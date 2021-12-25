'''
说明：用yield from实现协程并发
分析：
    假如执行方法req1需要2秒，执行req2需要1秒，这个时候，如果最终执行时间是3秒，则是同步执行；如果最终时间是2秒，则是并发执行，以下例子说明了

概念：send() 方法致使协程前进到下一个yield 语句

'''
import time
from collections import deque

_delay = deque()


class FutureX:
    def __init__(self, coro=None, delay_second=None):
        self.coro = coro
        if delay_second:
            self.start = delay_second + time.time()

    def step(self):
        coro = self.coro
        try:
            result = coro.send(None)
        except StopIteration as e:
            print(e.value)
            pass
        else:
            if isinstance(result, FutureX):
                _delay.append((self._wakeup, result))
            else:
                pass

    def _wakeup(self):
        self.step()

    def __iter__(self):
        yield self
        return None


def sleep0(seconds):

    future = FutureX(delay_second=seconds)
    b = yield from future
    return seconds


def req1():
    yield
    resp_time = yield from sleep0(2)
    return resp_time


def req2():
    yield
    resp_time = yield from sleep0(1)
    return resp_time


t1 = time.time()
f1, f2 = FutureX(req1()), FutureX(req2())
f1.step()
f1.step()

f2.step()
f2.step()


while _delay:
    callback, args = _delay.popleft()
    start = args.start
    if not start:
        continue
    while True:
        end = time.time()
        if start <= end:
            try:
                callback()
            except StopIteration as e:
                pass
            break

print(f'花费的时间：{round(time.time() - t1,1)}')

'''
结果:
2
1
花费的时间：2.0
'''