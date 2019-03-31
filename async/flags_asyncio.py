import asyncio
import aiohttp
from flags import BASE_URL, save_flag, show, main

#@asyncio.coroutine
async def get_flag(session, cc):
    url = '{}/{cc}.png'.format(BASE_URL, cc=cc.lower())
    #print(url)
    #resp = yield from aiohttp.request('GET', url)
    #image = yield from resp.read()
    async with session.get(url) as resp:
        image = await resp.read()
    return image

#@asyncio.coroutine
async def download_one(cc):
    #image = yield from get_flag(cc)
    async with aiohttp.ClientSession() as session:
        image = await(get_flag(session, cc))
    show(cc)
    save_flag(image, cc.lower() + '.png')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)

if __name__ == '__main__':
    main(download_many)