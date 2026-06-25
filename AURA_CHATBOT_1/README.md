<div align="center">

# 🤖 AURA — Custom AI Chatbot with Memory

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM%20API-F55036?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-3ddc84?style=for-the-badge)

> A conversational AI web app that remembers everything you say —
> built from scratch using Python, Flask, and the Groq LLM API.

</div>

---

## 🌟 What is this?

**Aura** is a full-stack AI chatbot web application with real in-session memory.
Unlike a basic chatbot that forgets you the moment you send a new message,
Aura keeps a growing history of your entire conversation and sends it to the
AI model on every turn — so it actually remembers your name, context, and
everything you've discussed.

This project was built phase by phase from the ground up, covering real
engineering concepts used in production AI applications today.

---

## 🧠 The Core Concept — How Memory Works

> LLMs are **stateless** by nature. Every API call is independent —
> the model has zero memory of what came before.

The trick behind conversational memory is entirely on **your side**:

```python
# Every turn follows these 3 steps:

# 1. Append the new user message to history
history.append({"role": "user", "content": user_input})

# 2. Send the ENTIRE history to the API — not just the latest message
response = client.chat.completions.create(model=MODEL, messages=history)

# 3. Append the model's reply so it's remembered next turn
history.append({"role": "assistant", "content": reply})
```

The model re-reads the full transcript every single time and responds
as if it remembers — because it literally just read everything again.

This maps directly to the formal definition from the project brief:
   
   Input (Mₜ ∪ Hₜ₋₁) → Process (GenAI SDK) → Output (Rₜ)

| Symbol | Meaning | In our code |
|--------|---------|-------------|
| `Mₜ` | Current user message | `user_input` |
| `Hₜ₋₁` | All previous messages | `history` list |
| `Rₜ` | Model's reply | `reply` |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **In-memory conversation history** | Full transcript resent to the API each turn |
| 🔒 **Per-user session isolation** | Each browser gets its own private history |
| 🎭 **4 Persona modes** | Assistant · Code Helper · Sarcastic Tutor · Creative Writer |
| 💬 **Typing indicator** | Animated dots while the model is thinking |
| 📋 **Copy button** | One-click copy on any bot message |
| ↓ **Export chat** | Download full conversation as `.txt` |
| 🌗 **Dark / Light mode** | Toggle between themes |
| ✂️ **History trimming** | Automatically drops oldest messages at 20 to prevent token overflow |
| 🛡️ **Friendly error handling** | Rate limits, context overflow, and server errors shown clearly |
| ⚡ **Request deduplication** | Blocks duplicate simultaneous requests per user |

---

## 🗂️ Project Structure

AURA_CHATBOT_1/

│

├── app.py                 # Flask server — routes, memory loop, session state

├── chatbot_terminal.py    # Terminal version — same memory logic, no web layer

├── test_connection.py     # Phase 1 smoke test — proves API key + SDK work

├── requirements.txt       # Python packages needed

├── .env                   # 🔒 Your secret API keys (never commit this)

├── .gitignore             # Tells Git what files to ignore

│

└── templates/

└── index.html         # Full chat UI — HTML + CSS + JavaScript

---

## 🚀 How to Run It

### 1. Clone or download the project

```bash
cd project_1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API keys

Create a `.env` file in the project folder:

GROQ_API_KEY=your_groq_api_key_here

SECRET_KEY=any_long_random_string_here

Get a free Groq API key (no credit card) at 👉 **console.groq.com/keys**

### 4. Test your connection first

```bash
python test_connection.py
```

You should see a one-line reply from the model confirming it's connected.

### 5. Run the terminal version (optional)

```bash
python chatbot_terminal.py
```

### 6. Run the full web app

```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000** 🎉

---

## 🎓 Key Concepts Learned

🔌 API Integration        Using an official SDK to connect to a frontier LLM

📦 Session State          Storing per-user data across stateless HTTP requests

🔄 Chat History Mechanics Append → resend full list → append reply, every turn

🌐 Flask Routing          How a web server maps URLs to Python functions

🤝 Frontend ↔ Backend     fetch() + JSON to pass messages between browser and server

🛡️ Error Handling         Catching API failures and surfacing them gracefully

🔒 Secret Management      Keeping API keys in .env, out of source code

✂️ Context Management     Trimming history to stay within model token limits

---

## 🔐 Security Notes

- ✅ API key stored in `.env`, never in code
- ✅ `.env` listed in `.gitignore` — will never be committed to Git
- ✅ Flask `SECRET_KEY` signs session cookies so users can't tamper with them
- ✅ Session isolation prevents one user's history leaking into another's

---

## 🔭 What Could Come Next

- 💾 **Persistent memory** — save conversations to SQLite so they survive server restarts
- 👤 **User accounts** — login system so each person has their own history across sessions
- 🌊 **Streaming replies** — show the bot's words appearing one by one as it generates them
- ☁️ **Deploy live** — host on Render or Railway so anyone can use it

---

<div align="center">

Built with 💚 using **Python · Flask · Groq · Llama 3.3**

</div>