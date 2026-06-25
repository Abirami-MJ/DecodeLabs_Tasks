import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not found. Add it to your .env file.")

client = Groq(api_key=api_key)
MODEL = "llama-3.3-70b-versatile"

# This list IS the chatbot's memory for the session.
# Each item: {"role": "user" or "assistant", "content": "..."}
history = []


def main():
    print("Chatbot ready (Groq + memory). Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        if not user_input:
            continue

        # 1. Append the new user message to history
        history.append({"role": "user", "content": user_input})

        # 2. Send the ENTIRE history to the API — not just this message
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=history,
            )
        except Exception as e:
            print(f"[Error talking to the API: {e}]\n")
            history.pop()  # don't keep a question that never got an answer
            continue

        reply = response.choices[0].message.content

        # 3. Append the model's reply to history too, so it's remembered next turn
        history.append({"role": "assistant", "content": reply})

        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    main()