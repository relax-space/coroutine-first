# 协程往事

根据`asyncio`制作了`asynciox`,并提供sleep方法,尽量不修改源代码的结构,`asynciox`支持本地运行和调试

## start
``` shell
python main.py
```

## asynciox使用

``` python
from asynciox.base_eventx import BaseEventLoop
from asynciox.taskx import gather, sleep

async def req1(loop):
    await sleep(1, loop=loop)
    return 1
async def req2():
    return 2

async def main(loop):
    res = await gather(req1(loop), req2(), loop=loop)
    print(res)

if __name__ == '__main__':
    loop = BaseEventLoop()
    BaseEventLoop().run_until_complete(main(loop))
```

## [asyncio 源码解读](docs/2.yield_from.md)

## More
1. [yield解读](docs/1.yield.md)

2. [yield from解读](docs/2.yield_from.md)

3. [async解读](docs/3.async.md)

4. [await解读](docs/4.await.md)

5. [让出控制权之yield流程](docs/5.yield_break.md)

6. [让出控制权之async流程](docs/6.async_break.md)

7. [协程并发之yield from流程](docs/7.yield_from_concurrent.md)

8. [协程并发之await流程](docs/8.await_concurrent.md)

9. [asyncio 源码解读](docs/9.asyncio.md)

10. [asyncio 体验](docs/10.asyncio_concurrent.md)

11. [asyncio 实战](docs/11.asyncio_sample.md)


:ribbon: :ribbon: 读后有收获可以作者喝咖啡：

<!-- ![](docs/aw2.png) -->
<img src="docs/aw2.png" width="60%"/>
