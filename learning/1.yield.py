'''
说明：yield的流程解释
概念：
    生成器：只要 Python 函数的定义体中有 yield 关键字，该函数就是生成器函数，调用生成器函数返回的是生成器对象
    yield：总得来说就是：产出和让步，产出结果，让出控制权
    send：send() 方法致使协程前进到下一个yield 语句，另外，生成器可以作为协程使用
'''


def yield1():
    '''
    整体解释：1是第一次send的返回值，b是第二次send的输入值，最后的return是最后一次的返回值
    '''
    b = yield 1
    return b


def yield2():
    yield


def yield3():
    yield 1


def print_value(f, args):

    try:
        b = f.send(args)
    except StopIteration as e:
        print(f'{f.__name__}返回值 {e.value}')
        return e.value
    else:
        print(f'{f.__name__}接收 {b}')


ys = [yield1(), yield2(), yield3()]
for y in ys:
    print_value(y, None)
    print_value(y, 2)

'''
结果:
yield1接收 1
yield1返回值 2
yield2接收 None
yield2返回值 None
yield3接收 1
yield3返回值 None
'''
