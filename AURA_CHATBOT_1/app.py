import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
from groq import Groq

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not found. Add it to your .env file.")

client = Groq(api_key=api_key)
MODEL = "llama-3.3-70b-versatile"

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback_dev_key")

PERSONAS = {
    "assistant": "You are Aura, a warm and friendly AI assistant. You are helpful, encouraging, and conversational. Keep responses clear and concise.",
    "coder":     "You are Aura, an expert programming assistant. Help with code, debugging, and technical concepts. Always use code blocks when showing code. Be precise and technical.",
    "tutor":     "You are Aura, a witty and slightly sarcastic but ultimately helpful tutor. You're clever and funny while still being genuinely educational. Challenge the user to think.",
    "writer":    "You are Aura, a creative writing assistant with flair and imagination. Help with stories, poems, scripts, and creative ideas. Be expressive and inspiring.",
}

# ── Phase 7: max number of messages to keep in memory ──
# Each exchange = 2 messages (1 user + 1 assistant).
# At 20 messages, we have 10 full exchanges — plenty of context
# without risking a context window overflow from the API.
MAX_HISTORY = 20


def trim_history(history):
    """
    If history exceeds MAX_HISTORY, drop the oldest exchange (2 messages)
    from the front. Keeps the conversation recent without crashing.
    We always drop in pairs (user + assistant) to keep the list balanced —
    the API expects alternating roles, so an odd trim would break that.
    """
    while len(history) > MAX_HISTORY:
        history = history[2:]  # drop oldest user + assistant pair
    return history


def friendly_error(e):
    """
    Phase 7: translate raw Groq API errors into readable messages
    so the user sees something useful instead of a raw stack trace.
    """
    msg = str(e).lower()

    if "rate limit" in msg or "429" in msg:
        return (
            "Aura is getting too many requests right now. "
            "Wait a few seconds and try again."
        )
    if "context" in msg or "tokens" in msg or "413" in msg:
        return (
            "This conversation has grown very long and hit the model's "
            "memory limit. Try clearing the chat to start fresh."
        )
    if "503" in msg or "502" in msg or "unavailable" in msg:
        return (
            "Groq's servers are temporarily unavailable. "
            "Try again in a moment."
        )
    if "401" in msg or "invalid api key" in msg:
        return (
            "API key issue — check that GROQ_API_KEY in your .env "
            "file is correct and hasn't expired."
        )

    # Fallback for anything unexpected
    return f"Something went wrong: {str(e)}"


@app.route("/")
def home():
    if "history" not in session:
        session["history"] = []
    if "persona" not in session:
        session["persona"] = "assistant"
    # Phase 7: reset the processing flag on every fresh page load
    session["is_processing"] = False
    return render_template("index.html")


@app.route("/set_persona", methods=["POST"])
def set_persona():
    persona = request.json.get("persona", "assistant")
    if persona not in PERSONAS:
        return jsonify({"error": "Unknown persona"}), 400
    session["persona"] = persona
    session["history"] = []
    session["is_processing"] = False
    return jsonify({"status": "ok", "persona": persona})


@app.route("/chat", methods=["POST"])
def chat():
    # ── Phase 7: block duplicate simultaneous requests ──
    # If this user's previous message is still being processed,
    # reject the new one cleanly rather than letting two API calls
    # race against the same history list.
    if session.get("is_processing", False):
        return jsonify({
            "error": "Still thinking about your last message — please wait."
        }), 429

    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    # Lock this user's session while we process
    session["is_processing"] = True

    history = session.get("history", [])
    persona = session.get("persona", "assistant")

    history.append({"role": "user", "content": user_input})

    messages_to_send = [
        {"role": "system", "content": PERSONAS[persona]}
    ] + history

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages_to_send,
        )
    except Exception as e:
        # Don't keep the user message if we never got a reply
        history.pop()
        session["history"] = history
        session["is_processing"] = False
        # Phase 7: return a friendly message, not a raw error
        return jsonify({"error": friendly_error(e)}), 500

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})

    # ── Phase 7: trim history before saving ──
    history = trim_history(history)

    session["history"] = history
    session["is_processing"] = False  # unlock

    # Let the frontend know if we've started trimming old messages
    is_trimmed = len(history) == MAX_HISTORY

    return jsonify({
        "reply": reply,
        "message_count": len(history),
        "is_trimmed": is_trimmed  # frontend can show a subtle notice
    })


@app.route("/clear", methods=["POST"])
def clear():
    session["history"] = []
    session["is_processing"] = False
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)