# --- add this block at the very top of streamlit_app.py ---
import sys
from pathlib import Path
ROOT = str(Path(__file__).resolve().parent.parent)  # project root
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
# ----------------------------------------------------------

import streamlit as st
from datetime import datetime
import time

from src.model_loader import ModelWrapper
from src.utils import save_image_with_metadata, apply_watermark
from src.content_filter import is_prompt_allowed
from src.config import DEFAULT_MODEL

st.set_page_config(page_title="AI Image Generator", layout="wide")
st.title("AI-Powered Text-to-Image Generator")

# Sidebar controls
with st.sidebar:
    model_id = st.text_input("Model ID", DEFAULT_MODEL)
    num_images = st.slider("Images per prompt", 1, 4, 1)
    width = st.selectbox("Width", [256, 384, 512, 768], index=2)
    height = st.selectbox("Height", [256, 384, 512, 768], index=2)
    steps = st.slider("Inference steps", 10, 50, 25)
    guidance = st.slider("Guidance scale", 1.0, 20.0, 7.5)
    seed = st.number_input("Seed (0 = random)", min_value=0, value=0)

prompt = st.text_area("Prompt", "a futuristic city at sunset, highly detailed, 4k, cinematic")
neg_prompt = st.text_area("Negative Prompt")

if st.button("Generate Images"):
    allowed, found = is_prompt_allowed(prompt)
    if not allowed:
        st.error(f"Blocked words detected: {found}")
    else:
        with st.spinner("Loading model..."):
            model = ModelWrapper(model_id)

        seed_val = None if seed == 0 else seed

        images = model.generate(
            prompt=prompt,
            negative_prompt=neg_prompt,
            width=width,
            height=height,
            num_images=num_images,
            guidance_scale=guidance,
            num_inference_steps=steps,
            seed=seed_val
        )

        cols = st.columns(num_images)

        for i, img in enumerate(images):
            img = apply_watermark(img)
            filename = f"generated_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{i}.png"

            out_path, meta_path = save_image_with_metadata(img, prompt, {
                "model": model_id,
                "width": width,
                "height": height,
                "steps": steps,
                "guidance": guidance,
                "seed": seed_val or "random"
            }, filename=filename)

            cols[i].image(img, caption=filename)
            cols[i].download_button("Download Image", open(out_path, "rb").read(), file_name=filename)

        st.success("Images generated successfully!")
