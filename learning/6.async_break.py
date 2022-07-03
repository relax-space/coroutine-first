

'''
协程中断：
    协程是如何中断交出控制权的？
分析：
    每一行程序都是按顺序一步一步执行的，如果有程序不是按顺序执行，表示曾经交出了控制权，以下的例子，本来应该应该顺序输出1,2，但是因为req1交出了控制权，所以，输出了2,1

概念：send() 方法致使协程前进到下一个yield 语句

'''

import time
from collections import deque

from asynciox.taskx import sleep

_delay = deque()


def sleep1():
    def sleep01():
        yield
        return None
    co = sleep01.__code__
    sleep01.__code__ = co.replace(co_flags=co.co_flags | 0x100)
    return sleep01()


def coroutine(func):
    co = func.__code__
    func.__code__ = co.replace(co_flags=co.co_flags | 0x100)
    return func


@coroutine
def sleep0():
    '''
    装饰器@：可以理解为 sleep0=coroutine(sleep0),意思就是sleep0函数执行之前，
    先调用coroutine方法执行一段内容之后，再把sleep0返回来
    '''
    yield
    return None


async def req1():
    b = await sleep0()
    return 1


async def req2():
    return 2


f1 = req1()
try:
    result = f1.send(None)
except StopIteration as e:
    print(f'正常打印 {e.value}')
    pass
else:
    _delay.append((f1, 1+time.time()))

f = req2()
try:
    f.send(None)
except StopIteration as e:
    print(f'正常打印 {e.value}')
    pass

for i, v in _delay:
    start = v
    while True:
        end = time.time()
        if start < end:
            try:
                result = i.send(None)
            except StopIteration as e:
                print(f'延迟打印 {e.value}')
                pass
            break
    pass

'''
结果:
正常打印 2
延迟打印 1
'''
