from pathlib import Path

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR.parent / "samples"
OUTPUT_DIR.mkdir(exist_ok=True)

DEFAULT_MODEL = "runwayml/stable-diffusion-v1-5"

MAX_WIDTH = 1024
MAX_HEIGHT = 1024
