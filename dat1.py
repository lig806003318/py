# -*- coding: utf-8
'''
classmates = ['riven', 'dog', 'frank']
name = classmates[-1]
print(name, "is dog!")
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]


print(L[0][0],L[1][1])


weight_xh = 68
height_xh = 1.76
bmi = weight_xh/(height_xh**2)
print(bmi)
if bmi < 18.5:
    print('BMI =', round(bmi, 2))
elif bmi < 25:
    print('BMI =', round(bmi, 2))
elif bmi < 28:
    print('BMI = %f, c' % bmi)
elif bmi < 29:
    print('BMI = %f, d' % bmi)
elif bmi > 32:
    print('BMI = %f, e' % bmi)
'''


sum = 0
for x in range(101):
    sum = sum + x
print(sum)
