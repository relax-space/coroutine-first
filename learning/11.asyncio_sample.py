import asyncio
import os

import aiofiles
from aiohttp import ClientSession, ClientTimeout, TCPConnector

'''
异步请求完整例子
1. 异步请求数据
2. 限制并发
3. 异步保存文件
'''


async def download(page: int, folder: str, session: ClientSession):
    url = 'https://catfact.ninja/facts'
    async with session.get(url, params={'page': page}) as resp:
        async with aiofiles.open(f'{folder}/{page}.json', mode='w') as f:
            await f.write(await resp.text())
            return page


async def trunks(sem, page: int, folder_name: str, session: ClientSession):
    async with sem:
        return await download(page, folder_name, session)


async def main():
    # 请求url参数列表
    url_pages = range(1, 5)
    # 创建文件夹data
    folder_name = 'data'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    # 限制并发数量
    sem = asyncio.Semaphore(50)
    # 异步请求，并保存到文件
    async with ClientSession(connector=TCPConnector(limit=5), timeout=ClientTimeout(300)) as session:
        tasks = []
        for page in url_pages:
            tasks.append(
                trunks(sem, page, folder_name, session))
        result = await asyncio.gather(*tasks)
        exp = set(url_pages)
        act = set(result)
        if exp == act:
            print(f'全部下载完成')
        else:
            print(f'未成功：{exp - act}，成功：{exp & act}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
