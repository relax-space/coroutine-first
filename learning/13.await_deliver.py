'''
await传递: 允许生成器或协程把工作委托给第三方完成
'''

'''
req3通过await进入了req1方法,而req2没能进入
'''


async def req1():
    return 1


async def req2():
    b = req1()
    return b


async def req3():
    b = await req1()
    return b


def print_value(f, args):

    try:
        b = f.send(args)
    except StopIteration as e:
        print(f'{f.__name__}返回值 {e.value}')
        return e.value
    else:
        print(f'{f.__name__}接收 {b}')


fs = [req2(), req3()]
for f in fs:
    print_value(f, None)

'''
输出:
    req2返回值 <coroutine object req1 at 0x000002AF9347C5C0>
        d:\1.source\pythonpath\coroutine-first\learning\13.await_deliver.py:37: RuntimeWarning: coroutine 'req1' was never awaited
        print_value(f, None)
        RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    req3返回值 1
'''
