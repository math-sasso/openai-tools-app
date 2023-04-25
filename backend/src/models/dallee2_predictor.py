import openai
from .base import BasePredictor

class DallePredictor():
    def __init__(self) -> None:
        pass

    def predict(self, text: str) -> str:
        response = openai.Image.create(
            prompt=text,
            n=1,
            size=256,
        )
        return response['choices'][0]['url']
    