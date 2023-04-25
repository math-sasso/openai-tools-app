from pydantic import BaseModel


class ImageGenerationRequest(BaseModel):
    prompt: str
    