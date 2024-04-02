import asyncio
from io import BytesIO

import aiohttp
from PIL import Image


async def get_image(session, url, local_id):
    async with session.get(url) as resp:
        content = await resp.content.read()
        Image.open(BytesIO(content)).save(f"artifacts/image{local_id}.png")
        return resp.status


async def main(number_of_images):
    async with aiohttp.ClientSession() as session:

        tasks = []
        for local_id in range(number_of_images):
            url = f'https://source.unsplash.com/random/200x200?sig=1'
            tasks.append(asyncio.ensure_future(get_image(session, url, local_id)))

        statuses = await asyncio.gather(*tasks)
        for status in statuses:
            print(status)


if __name__ == '__main__':
    asyncio.run(main(number_of_images=15))
