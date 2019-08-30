# -*- unicode:UTF-8 -*-
import os
print(list(range(1, 11)))

L = []
for x in list(range(1, 11)):
    L.append(x * x)

print(L)


print([b for b in os.listdir('.')])

