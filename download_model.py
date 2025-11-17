from diffusers import StableDiffusionPipeline
model_id = "stabilityai/stable-diffusion-2-1"  # you can change later
print("Starting download of", model_id)
StableDiffusionPipeline.from_pretrained(model_id, use_safetensors=True)
print("Model cached.")
