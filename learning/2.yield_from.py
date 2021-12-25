'''
说明：为了理解yield from，创建了fake_yield_from方法
概念：
功能1：在生成器 gen 中使用 yield from subgen()时，subgen 会获得控制权，把产出的值传给 gen 的调用方，即调用方可以直接控制 subgen。与此同时，gen 会阻塞，等待 subgen 终止。
功能2：猜测yield from subgen()的代码，等同于yield fake_yield_from(subgen())，如果是协程则send，否则如果是可迭代就next() str list tuple set map range
'''
import inspect


def subgen():
    res = yield 11
    return res


def gen():
    res = yield from subgen()
    return res


def fake_yield_from(f):
    # 模拟yield from的功能
    result = None
    if inspect.isgenerator(f):
        try:
            result = f.send(None)
        except StopIteration as e:
            result = e.value
    else:
        result = next(iter(f))
    return result


def gen_fake():
    res = yield fake_yield_from(subgen())
    return res


def print_value(f, args):
    try:
        b = f.send(args)
    except StopIteration as e:
        print(f'{f.__name__}返回值 {e.value}')
        return e.value
    else:
        print(f'{f.__name__}接收 {b}')


gs = [gen(), gen_fake()]
for g in gs:
    print_value(g, None)
    print_value(g, 2)

'''
结果:
gen接收 11
gen返回值 2
gen_fake接收 11
gen_fake返回值 2
'''
