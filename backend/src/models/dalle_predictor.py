import io
import os

import aiohttp
import openai
from PIL import Image

from .base import BasePredictor


class DallePredictor(BasePredictor):
    def __init__(self) -> None:
        pass

    async def ansyc_request_image(self, url: str) -> Image:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    buffer = io.BytesIO(await resp.read())
                    image = Image.open(buffer)
                else:
                    print("Exception Raised")
                    raise Exception(f"Ansyc request failed with status {resp.status}")
        return image

    async def predict(self, text: str) -> Image:
        openai.api_key = os.getenv("OPENAI_KEY")
        response = openai.Image.create(
            prompt=text,
            model="image-alpha-001",
            n=1,
            size="256x256",
        )
        url = response['data'][0]['url']

        img = await self.ansyc_request_image(url)
        return img
