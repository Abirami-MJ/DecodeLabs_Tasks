# ============================================================
#  generator.py — Gemini API Engine
#  Handles all communication with the Gemini API.
#  Applies inference parameters and returns generated copy.
# ============================================================

import google.generativeai as genai

from config        import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE, TOP_P, MAX_TOKENS
from prompt_builder import build_prompt

# ── CONFIGURE GEMINI ─────────────────────────────────────────
genai.configure(api_key=GEMINI_API_KEY)

# ── INFERENCE PARAMETERS ─────────────────────────────────────
generation_config = genai.types.GenerationConfig(
    temperature      = TEMPERATURE,   # Creativity level (0.0 - 1.0)
    top_p            = TOP_P,         # Vocabulary diversity (0.0 - 1.0)
    max_output_tokens= MAX_TOKENS     # Maximum length of response
)

# ── INITIALIZE MODEL ─────────────────────────────────────────
model = genai.GenerativeModel(
    model_name        = MODEL_NAME,
    generation_config = generation_config
)

# ── MAIN GENERATION FUNCTION ─────────────────────────────────
def generate_copy(product_name, description, platform, tone):
    """
    Generates marketing copy using Gemini API.

    Args:
        product_name (str) : Name of the product
        description  (str) : Raw product description
        platform     (str) : Target platform (LinkedIn/Instagram/Email)
        tone         (str) : Desired tone (Professional/Playful/etc.)

    Returns:
        str: Generated marketing copy or error message
    """

    try:
        # Build the dynamic prompt
        prompt = build_prompt(product_name, description, platform, tone)

        # Send to Gemini & get response
        response = model.generate_content(prompt)

        # Extract and return the text
        return response.text.strip()

    except Exception as e:
        # Handle errors gracefully without crashing
        error_message = str(e)

        if "API_KEY_INVALID" in error_message:
            return "❌ Error: Invalid API key. Please check config.py"

        elif "quota" in error_message.lower():
            return "❌ Error: Rate limit reached. Please wait a minute and try again."

        elif "not found" in error_message.lower():
            return "❌ Error: Model not found. Please check MODEL_NAME in config.py"

        else:
            return f"❌ Unexpected error: {error_message}"


# ── MULTI PLATFORM GENERATION ────────────────────────────────
def generate_all_platforms(product_name, description, tone, platforms):
    """
    Generates copy for multiple platforms in one run.

    Args:
        product_name (str)  : Name of the product
        description  (str)  : Raw product description
        tone         (str)  : Desired tone
        platforms    (list) : List of platforms to generate for

    Returns:
        dict: Platform name as key, generated copy as value
    """

    results = {}

    for platform in platforms:
        print(f"   Generating {platform} copy...", end=" ", flush=True)
        results[platform] = generate_copy(product_name, description, platform, tone)
        print("✅")

    return results