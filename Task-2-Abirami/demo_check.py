import google.generativeai as genai

# ── 1. YOUR API KEY ──────────────────────────────────────────
API_KEY = "AQ.Ab8RN6IFwx1xytm27XVqdytVHVZ8D7n02GxMCOq9RS2NLloRmw"
genai.configure(api_key=API_KEY)

# ── 2. MODEL SETUP ───────────────────────────────────────────
model = genai.GenerativeModel("gemini-3.5-flash")

# ── 3. AVAILABLE OPTIONS ─────────────────────────────────────
PLATFORMS = ["LinkedIn", "Instagram", "Email"]
TONES     = ["Professional", "Playful", "Urgent", "Inspirational"]

# ── 4. DYNAMIC PROMPT TEMPLATE ───────────────────────────────
def build_prompt(product_name, description, platform, tone):
    return f"""
You are an expert marketing copywriter.
Your job is to write compelling {platform} marketing copy.

Product Name : {product_name}
Description  : {description}
Tone         : {tone}

Platform rules:
- LinkedIn : Professional, 150-200 words, include a call to action
- Instagram : Catchy, under 100 words, include 5 relevant hashtags
- Email     : Subject line + body, persuasive, under 200 words

Write ONLY the final copy. No explanations. No labels.
"""

# ── 5. GENERATE COPY ─────────────────────────────────────────
def generate_copy(product_name, description, platform, tone):
    prompt = build_prompt(product_name, description, platform, tone)
    response = model.generate_content(prompt)
    return response.text

# ── 6. TEST RUN ──────────────────────────────────────────────
if __name__ == "__main__":

    product_name = "EcoBottle Pro"
    description  = "A reusable water bottle with UV self-cleaning technology and temperature control"
    platform     = "Instagram"
    tone         = "Playful"

    print("\n Generating copy...\n")
    result = generate_copy(product_name, description, platform, tone)
    print("=" * 50)
    print(result)
    print("=" * 50)