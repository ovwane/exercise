# -*- coding:gbk -*-
'''''ʾ��7: ��ʾ��4�Ļ����ϣ���װ������������ 
����һʾ�������������һ���װ�� 
װ�κ�����ʵ����Ӧ��������Щ'''


def deco(arg):
    def _deco(func):
        def __deco():
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco

    return _deco


@deco(u"��¼����")
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
