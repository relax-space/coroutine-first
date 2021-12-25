
'''
说明：实现同样的功能，yield要比async写更多的代码
概念：
    async与yield：
        1.区别：
            1.1 yield语法比较复杂，async语法简单
                yield：b=yield a，yield右边的a是第一次的返回值，左边的b是第二次执行的输入值，最后还有一个return是最后一次返回值
                async：async修饰的方法，在做send参数的时候，只能传None，这大大的简化了send输入参数的逻辑
            1.2 async不需要只需要send一次就可以获得返回值，yield要send2次
            
        2.相同点：都可以实现阻塞的功能
        
'''


async def req1(param):
    return param


def req2(param):
    res = yield param
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
req1返回值 1
req2接收 2
req2返回值 2
'''