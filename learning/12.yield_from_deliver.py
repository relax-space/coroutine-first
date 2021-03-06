'''
yield from传递: 允许生成器或协程把工作委托给第三方完成
'''

'''
req3通过yield from进入到了req1的yield,而req2没能进入
'''


def req1():
    yield 1.1
    return 1


def req2():
    yield
    b = req1()
    return b


def req3():
    yield
    b = yield from req1()
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
    print_value(f, None)

'''
输出:
    req2接收 None
    req2返回值 <generator object req1 at 0x000002901A364430>
    req3接收 None
    req3接收 1.1
'''
