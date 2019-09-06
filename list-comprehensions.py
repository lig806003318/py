# -*- unicode: UTF-8 -*-
'''
list comprehension 列表生成式
comprehension[ˌkɒmprɪˈhenʃn]  n.理解力;领悟能力

print(list(range(1, 11)))
def a():
    L = []
    for i in range(1, 11):
        L.append(i * i)
    print(L)
a()
简写
print([x * x for x in range(1,11)])
全排列
print([m + n for m in 'ABC' for n in 'ABC'])
['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
遍历key和value
d = {'x':'A', 'y':'B'}
for k, v in d.items():
    print(k, '=', v)
x = A
y = B

print(isinstance(1, str))
判断List是字符串变成小写。
L = ['AAAA', 'World', 18, 'Apple']
def a(b):
    for i in b:        
        if isinstance(i, str) == 1:
            print(i.lower())
        else:
            print('aaaaaaaa')
a(L)
False
aaaa
world
aaaaaaaa
apple
'''


