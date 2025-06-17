import asyncio, numpy, concurrent.futures

def start(all, packs):
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as pool:
        return pool.map(thread, numpy.array_split(all, packs))
def thread(pack):
    asyncio.set_event_loop(asyncio.new_event_loop())
    return asyncio.get_event_loop().run_until_complete(asyncio.gather(*[download(a) for a in pack]))
async def download(date):
    await asyncio.sleep(2)
    return date

result = start(range(1000), 10)
