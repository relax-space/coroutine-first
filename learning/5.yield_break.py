

'''
说明：用yield from实现协程中断交出控制权
分析：
    每一行程序都是按顺序一步一步执行的，如果有程序不是按顺序执行，表示曾经交出了控制权，以下的例子，本来应该应该顺序输出1,2，但是因为req1交出了控制权，所以，输出了2,1

'''

import time
from collections import deque

_delay = deque()


def sleep0():
    yield
    return None


def req1():
    yield
    b = yield from sleep0()
    return 1


def req2():
    yield
    return 2


f1 = req1()
f1.send(None)
try:
    result = f1.send(None)
except StopIteration as e:
    print(f'正常打印 {e.value}')
    pass
else:
    _delay.append((f1, 1+time.time()))

f = req2()
f.send(None)
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
