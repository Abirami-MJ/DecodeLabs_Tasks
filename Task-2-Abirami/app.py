# ============================================================
#  app.py — CopyFlow Web UI
#  Browser-based interface powered by Streamlit.
#  Reuses all existing modules (config, prompt, generator)
# ============================================================

import streamlit as st
from config    import PLATFORMS, TONES, APP_NAME, APP_VERSION, APP_TAGLINE
from generator import generate_copy, generate_all_platforms

# ── PAGE CONFIGURATION ───────────────────────────────────────
st.set_page_config(
    page_title = f"{APP_NAME} — AI Copy Generator",
    page_icon  = "✦",
    layout     = "centered"
)

# ── CUSTOM CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #0f0f0f;
        color: #ffffff;
    }

    /* Banner */
    .banner {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    .banner h1 {
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 2px;
    }
    .banner p {
        color: #888888;
        font-size: 1rem;
        letter-spacing: 1px;
    }

    /* Section headers */
    .section-title {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 2px;
        color: #888888;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        margin-top: 1.5rem;
    }

    /* Result card */
    .result-card {
        background-color: #1a1a1a;
        border: 1px solid #2a2a2a;
        border-left: 3px solid #ffffff;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .result-platform {
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 2px;
        color: #888888;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }
    .result-copy {
        color: #e0e0e0;
        font-size: 0.95rem;
        line-height: 1.7;
        white-space: pre-wrap;
    }

    /* Generate button */
    .stButton > button {
        width: 100%;
        background-color: #ffffff;
        color: #000000;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 1px;
        padding: 0.75rem;
        border: none;
        border-radius: 6px;
        margin-top: 1.5rem;
        cursor: pointer;
        transition: opacity 0.2s;
    }
    .stButton > button:hover {
        opacity: 0.85;
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #2a2a2a;
        border-radius: 6px;
    }

    /* Selectbox */
    .stSelectbox > div > div {
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #2a2a2a;
        border-radius: 6px;
    }

    /* Divider */
    hr {
        border-color: #2a2a2a;
        margin: 2rem 0;
    }

    /* Mode radio */
    .stRadio > label {
        color: #888888;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# ── BANNER ───────────────────────────────────────────────────
st.markdown(f"""
<div class="banner">
    <h1>✦ {APP_NAME}</h1>
    <p>{APP_TAGLINE} — v{APP_VERSION}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── PRODUCT DETAILS ──────────────────────────────────────────
st.markdown('<p class="section-title">Product Details</p>', unsafe_allow_html=True)

product_name = st.text_input(
    label       = "Product Name",
    placeholder = "e.g. EcoBottle Pro"
)

description = st.text_area(
    label       = "Product Description",
    placeholder = "e.g. A reusable water bottle with UV self-cleaning technology...",
    height      = 120
)

# ── TONE & PLATFORM ──────────────────────────────────────────
st.markdown('<p class="section-title">Tone & Platform</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tone = st.selectbox("Tone", TONES)

with col2:
    mode = st.radio(
        "Generation Mode",
        ["Single Platform", "All Platforms"],
        horizontal = True
    )

if mode == "Single Platform":
    platform = st.selectbox("Platform", PLATFORMS)

# ── GENERATE BUTTON ──────────────────────────────────────────
generate = st.button("⚡ GENERATE COPY")

# ── OUTPUT ───────────────────────────────────────────────────
if generate:

    # Validation
    if not product_name.strip():
        st.error("⚠️ Please enter a product name.")
    elif not description.strip():
        st.error("⚠️ Please enter a product description.")

    else:
        st.markdown("---")
        st.markdown('<p class="section-title">Generated Copy</p>', unsafe_allow_html=True)

        if mode == "Single Platform":
            with st.spinner(f"Generating {platform} copy..."):
                copy = generate_copy(product_name, description, platform, tone)

            st.markdown(f"""
            <div class="result-card">
                <div class="result-platform">✦ {platform}</div>
                <div class="result-copy">{copy}</div>
            </div>
            """, unsafe_allow_html=True)

            # Copy button
            st.code(copy, language=None)

        elif mode == "All Platforms":
            with st.spinner("Generating copy for all platforms..."):
                results = generate_all_platforms(
                    product_name, description, tone, PLATFORMS
                )

            for plat, copy in results.items():
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-platform">✦ {plat}</div>
                    <div class="result-copy">{copy}</div>
                </div>
                """, unsafe_allow_html=True)

                st.code(copy, language=None)
                st.markdown("")

# ── FOOTER ───────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<p style="text-align:center; color:#444444; font-size:0.75rem; letter-spacing:1px;">
    COPYFLOW ✦ POWERED BY GEMINI AI ✦ 100% FREE
</p>
""", unsafe_allow_html=True)