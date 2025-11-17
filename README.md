AI IMAGE GENERATOR – TEXT TO IMAGE USING STABLE DIFFUSION

Description:
This project is a complete text-to-image generation system built using open-source diffusion models, PyTorch, and Streamlit.
Users can enter text prompts, and the application generates corresponding images.
The system supports metadata saving, watermarking, and adjustable generation parameters.
This project demonstrates hands-on knowledge of Generative AI, prompt engineering, and model deployment.

FEATURES

Generate images from text prompts

Uses Stable Diffusion v1.5 (runwayml/stable-diffusion-v1-5)

Streamlit web interface

Adjustable parameters:

Image size

Number of inference steps

Guidance scale

Number of images

Seed value

Automatic saving of images with metadata

Watermark added for responsible AI usage

Basic content filtering for unsafe prompts

Fully CPU-compatible, optional GPU support

TECHNOLOGY STACK

Python
PyTorch
HuggingFace Diffusers
Streamlit
Pillow
JSON
Open-source Stable Diffusion model

PROJECT STRUCTURE

ai_image_generator/
src/
streamlit_app.py
model_loader.py
utils.py
config.py
content_filter.py
samples/ (generated images and metadata)
download_model.py
test_generate.py
requirements.txt
.gitignore
README.txt (this file)
venv/ (excluded from upload)

INSTALLATION AND SETUP

Open a terminal inside the project folder.

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
CMD:
venv\Scripts\activate.bat
PowerShell:
venv\Scripts\Activate.ps1

Install all required libraries:
pip install -r requirements.txt

Download the Stable Diffusion model:
python download_model.py

RUNNING THE APPLICATION

Start the Streamlit application:
streamlit run src/streamlit_app.py

Then open:
http://localhost:8501

EXAMPLE PROMPTS

a futuristic city at sunset, highly detailed
a robot painted in Van Gogh style
a magical glowing forest, cinematic lighting
an astronaut riding a horse, photorealistic

PROMPT ENGINEERING TIPS

Use quality modifiers:
ultra-detailed
cinematic lighting
digital painting
high resolution

Avoid vague prompts.
Be specific about style, lighting, and subject.

ETHICAL GUIDELINES

Images are watermarked with “AI-generated”.
Unsafe prompts are filtered.
For educational and research use only.
Avoid generating misleading or harmful content.

TROUBLESHOOTING

If generation is slow:
Use smaller image size (256x256)
Reduce steps to 10–20

CUDA not available:
Install CUDA-enabled PyTorch if you have an NVIDIA GPU

Module errors:
Make sure venv is activated

FUTURE IMPROVEMENTS

GPU acceleration
SDXL or Flux model support
Image upscaling
Batch prompt generation
Advanced content filtering
Custom fine-tuning
API support

AUTHOR

(Replace with your details)
Your Name
Data Science with Generative AI
Frontline Edutech
