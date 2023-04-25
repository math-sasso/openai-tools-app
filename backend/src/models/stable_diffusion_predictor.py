import torch
from diffusers import StableDiffusionPipeline
from .base import BasePredictor

class StableDiffusionPredictor(BasePredictor):
    def __init__(self, model_id:str) -> None:
        model_id = "runwayml/stable-diffusion-v1-5"
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id,torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")

    def predict(
        self,
        prompt:str = ""
    ):
        if not prompt:
            raise ValueError("Please provide a text")
        image = self.pipe(prompt).images[0]
        return image
        


