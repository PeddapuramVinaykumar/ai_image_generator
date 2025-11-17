import json
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from src.config import OUTPUT_DIR


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def save_image_with_metadata(img, prompt, params, filename=None):
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    if filename is None:
        filename = f"image_{timestamp}.png"

    out_path = OUTPUT_DIR / filename
    img.save(out_path)

    meta = {
        "prompt": prompt,
        "params": params,
        "timestamp": timestamp
    }
    meta_path = out_path.with_suffix(".json")

    with open(meta_path, "w", encoding="utf8") as f:
        json.dump(meta, f, indent=2)

    return out_path, meta_path


def apply_watermark(img, text="AI-generated"):
    drawable = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    w, h = img.size
    margin = 8
    drawable.text((margin, h - 20), text, fill=(255, 255, 255), font=font)
    return img
