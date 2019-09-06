# -*- unicode=UTF-8 -*-
'''
斐波拉契数列
1, 1, 2, 3, 5, 8, 13, 21, 34
def fib(max):
    a, b, c = 0, 0, 1
    while a < max:
        print(c)
        b, c = c, b + c
        a = a + 1
    return 'done'
fib(6)

'''

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)