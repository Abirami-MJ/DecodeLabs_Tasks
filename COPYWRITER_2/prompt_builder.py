# ============================================================
#  prompt_builder.py — Dynamic Prompt Template Builder
#  Constructs structured prompts by injecting user inputs
#  and platform rules into a reusable template.
# ============================================================

from config import PLATFORM_RULES

# ── SYSTEM PERSONA ───────────────────────────────────────────
SYSTEM_PERSONA = """
You are CopyFlow, an elite marketing copywriter with 15+ years
of experience across digital platforms. You write copy that
converts readers into customers. You deeply understand platform
culture, audience psychology, and brand voice.
"""

# ── MAIN PROMPT BUILDER ──────────────────────────────────────
def build_prompt(product_name, description, platform, tone):
    """
    Builds a structured prompt by injecting:
    - Product details (name + description)
    - Target platform (LinkedIn / Instagram / Email)
    - Desired tone (Professional / Playful / Urgent / Inspirational)
    - Platform-specific writing rules from config.py

    Returns:
        str: A fully compiled prompt string ready for Gemini
    """

    platform_rule = PLATFORM_RULES.get(platform, "Write compelling marketing copy.")

    prompt = f"""
{SYSTEM_PERSONA}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Write {platform} marketing copy for the product below.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRODUCT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Product Name  : {product_name}
Description   : {description}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tone          : {tone}
Platform Rule : {platform_rule}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Write ONLY the final copy
- No explanations, no labels, no preamble
- Do not say "Here is your copy" or similar
- Start directly with the marketing content
"""
    return prompt