# -*- unicode:UTF-8 -*-
'''
def add_end(L=[]):
    L.append('frank')
    return L
print(add_end())


def calc(*aa):
    sum = 0
    for n in aa:
        sum = sum + n * n
    return sum


print(calc(1, 2))
L = [1, 2]
print(calc(*L))
print(person('riven', 30, city='beijing'))
'''


def person(name, age, **ab):
    print('name:', name, 'age:', age, 'other:', ab)


print(person('riven', 18, city='beijing'))

extra = {'city': 'beijing', 'job': 'Engineer'}

print(person('riven', 18, city=extra['city'], job=extra['job']))
