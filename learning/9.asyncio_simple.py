import asyncio


async def req1():
    await asyncio.sleep(1)
    return 1


async def req2():
    return 2


async def main():
    res = await asyncio.gather(req1(), req2())

    print(res)

asyncio.get_event_loop().run_until_complete(main())
