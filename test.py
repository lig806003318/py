# -*- unicode=UTF-8 -*-

'''
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 4)
print(f())
'''
a = range(1, 3)
for i in a:
    print(i)
