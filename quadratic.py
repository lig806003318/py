# -*- coding: utf-8 -*-
import math
print(math.sqrt(4))


def quadratic(a, b, c):
    dt = math.sqrt(b*b - 4*a*c)
    x1 = (-b + dt)/(2 * a)
    x2 = (-b - dt)/(2 * a)
    return x1, x2


print(quadratic(2, 5, 4))
