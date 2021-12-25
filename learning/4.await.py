
'''
说明：分别用await和yield from实现了同样功能
概念：
    await与yield from：
        1.区别： yield from 后面值，要么是None，要么是最终为可迭代对象，而await后面只能跟async开头的方法
        2.相同点：都是产出结果，让出控制权，等待返回结果
        
'''


async def req1_sub(param):
    return param+10


async def req1(param):
    res = await req1_sub(param)
    res += 100
    return res


def req2_sub(param):
    res = yield param+10
    return res


def req2(param):
    res = yield from req2_sub(param)
    res += 100
    return res


def print_value(f, args):
    try:
        b = f.send(args)
    except StopIteration as e:
        print(f'{f.__name__}返回值 {e.value}')
        return e.value
    else:
        print(f'{f.__name__}接收 {b}')
        return b


g1 = req1(1)
print_value(g1, None)


g2 = req2(2)
res = print_value(g2, None)
print_value(g2, res)

'''
结果:
req1返回值 111
req2接收 12
req2返回值 112
'''