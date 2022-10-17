import aiohttp
from .config import url, user, password
buttons = []


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=aiohttp.BasicAuth(user, password)) as res:
            return await res.json()


async def key():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=aiohttp.BasicAuth(user, password)) as res:
            data = await res.json()
            for x in data:
                name = x['name']
                if x['add_bot_button']:
                    buttons.append(name)

