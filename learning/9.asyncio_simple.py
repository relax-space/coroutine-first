import asyncio


async def req1():
    await asyncio.sleep(1)
    print('执行 req1')
    return 1


async def req2():
    print('执行 req2')
    return 2


async def main():
    list = [req1(), req2()]
    res = await asyncio.gather(*list)
    '''
    虽然,req2是先执行完的, 
    但是res返回值的顺序, 还是跟list顺序保持一致
    '''
    print(res)


asyncio.get_event_loop().run_until_complete(main())
'''
结果:
执行 req2
执行 req1
[1, 2]
'''
