# -*- coding:gbk -*-
'''''示例7: 在示例4的基础上，让装饰器带参数， 
和上一示例相比在外层多了一层包装。 
装饰函数名实际上应更有意义些'''


def deco(arg):
    def _deco(func):
        def __deco():
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco

    return _deco


@deco(u"登录测试")
def myfunc():
    pass



@deco("module2")
def myfunc2():
    pass

myfunc()
myfunc2()
#
# def deco(abc):
#     def wrapper(a):
#         print('''called:
#         function: %s
#         args :%r
#         kargs:%r''')
#         print '%s' % a
#     return wrapper
#
#
#
# @deco('abc')
# def hello():
#     print('hello')
#
# hello()
