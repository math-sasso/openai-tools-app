import io
import aiohttp
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
        # openai.api_key = os.getenv("OPENAI_KEY")
        # response = openai.Image.create(
        #     prompt=text,
        #     model="image-alpha-001",
        #     n=1,
        #     size="256x256",
        # )
        # url = response['data'][0]['url']

        url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-xFxkq2W7W5xOyDkaxbprZ4yl/user-OppN4epsHjDum5Hp0lRxGagh/img-oEDd0Shal9KyoJAqZjW22vGo.png?st=2023-04-25T18%3A05%3A31Z&se=2023-04-25T20%3A05%3A31Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-25T19%3A01%3A39Z&ske=2023-04-26T19%3A01%3A39Z&sks=b&skv=2021-08-06&sig=zQuMYYIXJ3pzeOnDcdkeGG/YCVt/VgBEXhSmsfURRTg%3D"
        img = await self.ansyc_request_image(url)
        return img
