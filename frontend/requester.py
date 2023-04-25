import aiohttp


async def request_image(prompt):
    async with aiohttp.ClientSession() as session:
        async with session.get(prompt) as response:
            if response.status == 200:
                return await response.read()
            else:
                return None