import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

class ModelWrapper:
    def __init__(self, model_id, device=None):
        self.model_id = model_id
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self._load_pipeline()

    def _load_pipeline(self):
        print(f"Loading model {self.model_id} on {self.device}...")

        pipe = StableDiffusionPipeline.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            safety_checker=None,
            use_safetensors=True
        )

        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe = pipe.to(self.device)

        try:
            pipe.enable_xformers_memory_efficient_attention()
        except:
            pass

        self.pipe = pipe

    def generate(self, prompt, negative_prompt=None, width=512, height=512,
                 num_images=1, guidance_scale=7.5, num_inference_steps=25, seed=None):

        generator = None
        if seed is not None:
            generator = torch.Generator(device=self.device).manual_seed(seed)

        results = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            guidance_scale=guidance_scale,
            num_inference_steps=num_inference_steps,
            num_images_per_prompt=num_images,
            generator=generator
        )

        return results.images
