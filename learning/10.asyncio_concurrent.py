'''
说明：
    1. 测试2个请求并发的时间，要比同步执行的时间短
    2. 测试中的api用的是延迟请求，每个请求至少耗费1.5秒
'''

import asyncio
import time

import requests
from aiohttp import ClientSession


async def fetch(session, param):
    async with session.get(f'https://deelay.me/{param*1000}/http://httpbin.org/get?a={param}') as resp:
        data = await resp.json()
        print(data['args']['a'])
        return data


async def req_async():
    async with ClientSession() as session:
        return await asyncio.gather(fetch(session, 2), fetch(session, 1))


def req():
    session = requests.Session()
    p1, p2 = 2, 1
    return [session.get(f'https://deelay.me/{p1*1000}/http://httpbin.org/get?a={p1}').json(),
            session.get(f'https://deelay.me/{p2*1000}/http://httpbin.org/get?a={p2}').json()]


async def main():
    s1 = time.time()
    v1 = await req_async()
    s2 = time.time()
    v2 = req()
    print(f'异步请求时间：{round(s2-s1,1)}s    响应结果:{[v["args"]["a"] for v in v1]}')
    print(
        f'同步请求时间：{round(time.time()-s2,1)}s    响应结果:{[v["args"]["a"] for v in v2]}')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
