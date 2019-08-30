# -*- unicode= UTF-8 -*-
'''
###**kw定义参数个数不受限制， 然后最后传入参数使用**listname为简略写法
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other: ', kw)
print(person('Bob', 30, city='北京'))
extra = {'city': 'Beijing', 'job': 'Engineer'}

print(person('Bob', 30, **extra))

##**kw这样定义传入参数不受限制，下面例子传入了addr也可以显示
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other', kw)
print(person('riven', 18, addr='chaoyang'))



##指定参数限制为这种写法，如图  参入参数必须为限定的， 
def person(name, age, *, city, job):
    print(name, age, city, job)


##把**extra dir 参数传入函数中

print(person('riven', 17, **extra))


##自定义函数-多参数（不确定个数）  
传入变量可以是list ,caple
def calc(*aa):
    sum = 0
    for n in aa:
        sum = sum + n * n
    return sum
print(calc(1, 2))
传入list使用*      
L = [1, 3]
print(calc(*L))

'''


def f1(a, b, c=0, *args, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'args=', args, 'kw=', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'kw:', kw)


print()


args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}

print(f2(*args, **kw))
