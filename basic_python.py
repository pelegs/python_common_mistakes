# ----- Variables and print ----- #
n = 3
x = 2.5 + 0.1
z = 1 + 2j
s = "something"
b = True and False
print(n, x, z, s, b)
# print(n + x)
# print(s + n)
# print(s + str(n))

# ----- Lists and dictionaries ----- #
l = [1, 2, -3, 'a', False, 7.5]
print(l)
print(l[-1])
l += [0, 0]
print(l)
del(l[1])
print(l)

capitals = {
    'Germany': 'Berlin',
    'France': 'Paris',
    'Italy': 'Rome',
    'Canada': 'Ottawa',
    'Sweden': 'Stockholm',
    'The Netherlands': 'not the Hague',
}
print(capitals['Germany'])

# ----- Conditionals ----- #
a = 2
b = 1.5
if a > b:
    print('a is bigger')
elif a < b:
    print('b is bigger')
else:
    print('a equals b')

# ----- Loops ----- #
for i in range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

for i in range(10):
    if i == 5:
        break
    print(i)

# ----- Functions ----- #
def sqr(n):
    return n**2

print(sqr(10))

# ----- External libraries ----- #
import numpy as np
print(np.sqrt(100))

import itertools
X = ['a', 'b']
for x in itertools.product(X, repeat=3): # X^3
    print(x)

from itertools import permutations as perms
A = [1, 2, 3, 4]
for a in perms(A):
    print(a)
