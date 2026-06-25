# ✦ CopyFlow — AI-Powered Marketing Copy Generator
> Version 1.0.0 | Powered by Google Gemini AI | 100% Free

---

## 👋 Hey Future Me — Here's What This Project Is

CopyFlow is a Python application I built that automatically generates
professional marketing copy for different platforms using Google's
Gemini AI. You give it a product name and description, pick a tone
and platform — and it writes the copy for you instantly.

**Example:** Give it "EcoBottle Pro — a UV self-cleaning water bottle"
and it generates a LinkedIn post, Instagram caption, and Email campaign
all in one click.

---

## 🗂️ Project Structure

```
copywriter_ai/
├── app.py               → Web UI (run this for browser interface)
├── copyflow.py          → CLI version (run this for terminal interface)
├── config.py            → YOUR API KEY + all settings live here
├── generator.py         → Handles all Gemini API communication
├── prompt_builder.py    → Builds dynamic prompts from user inputs
├── requirements.txt     → All Python libraries needed
├── .gitignore           → Tells Git what NOT to upload (keeps key safe)
└── README.md            → This file
```

---

## ⚙️ How It Works (Simple Explanation)

```
You enter product details
        ↓
prompt_builder.py builds a structured prompt
        ↓
generator.py sends it to Gemini API
        ↓
Gemini generates the marketing copy
        ↓
App displays it on screen
```

---

## 🚀 How To Run This Project

### Step 1 — Get your FREE Gemini API Key
- Go to https://aistudio.google.com
- Click "Get API Key"
- Copy the key (starts with AIza...)

### Step 2 — Add your API key
- Open `config.py`
- Find this line:
```python
GEMINI_API_KEY = "paste_your_gemini_api_key_here"
```
- Replace with your actual key

### Step 3 — Install libraries
```
py -3.14 -m pip install -r requirements.txt
```

### Step 4 — Run the Web UI (Recommended)
```
py -3.14 -m streamlit run app.py
```
Then open your browser at: http://localhost:8501

### Step 5 — OR Run the Terminal Version
```
py -3.14 copyflow.py
```

---

## 🎛️ Settings You Can Change (config.py)

| Setting | What it does | Default |
|---|---|---|
| `TEMPERATURE` | 0.0 = focused, 1.0 = creative | 0.8 |
| `TOP_P` | Vocabulary diversity | 0.9 |
| `MAX_TOKENS` | Maximum length of output | 512 |
| `MODEL_NAME` | Which Gemini model to use | gemini-3.5-flash |

---

## 🌐 Platforms Supported

| Platform | What it generates |
|---|---|
| LinkedIn | 150-200 words, professional, with call to action |
| Instagram | Under 100 words, catchy, with 5 hashtags |
| Email | Subject line + persuasive body, under 200 words |

---

## 🎨 Tones Available

- **Professional** — Formal, business-like
- **Playful** — Fun, energetic, uses emojis
- **Urgent** — Creates FOMO, drives action fast
- **Inspirational** — Motivational, emotional, uplifting

---

## 💰 Cost

**Completely FREE.**
- Google Gemini API free tier: 1,500 requests/day
- No credit card required
- Get key at: https://aistudio.google.com

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.14 | Core programming language |
| Google Gemini API | AI model for generating copy |
| Streamlit | Web UI framework |
| google-generativeai | Official Gemini Python SDK |

---

UI Image:

<img width="1433" height="818" alt="image" src="https://github.com/user-attachments/assets/aaf51788-181c-402b-8d2a-b5e7ad4cd1a6" />

<img width="1146" height="836" alt="image" src="https://github.com/user-attachments/assets/a92c29d4-70d1-4f8a-bbf1-558baedfe4c4" />

<img width="1127" height="842" alt="image" src="https://github.com/user-attachments/assets/345e9d57-629c-4d05-90c0-b0400a34d7d8" />



## 📝 Key Concepts I Used In This Project

- **Dynamic Prompt Templates** — Injecting variables into prompts
- **Inference Parameters** — Temperature & Top_P to control AI creativity
- **Modular Code Structure** — Splitting code into focused files
- **Error Handling** — App never crashes, always shows friendly messages
- **Streamlit UI** — Turning a Python script into a web app

---

## 🔒 Security Note

- Your API key lives only in `config.py`
- `config.py` is listed in `.gitignore`
- This means if you push to GitHub, your key stays private and safe
- Never share your `config.py` file with anyone

---

*Built with 💙 by Abirami  | CopyFlow v1.0.0*
