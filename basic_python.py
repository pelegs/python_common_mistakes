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

# ----- Strings ----- #
# ' vs "... there is no difference!
txt1 = "I'm a text, and I can use single quotes. Double quotes, i.e. \", must be escaped."
txt2 = 'I\'m also a text! Here\'s a quote: "bla bla bla".'

# Multiline strings
mltxt1 = """
I'm a string with several lines.
It's easy to use me :)
Have a nice day!
"""
print(mltxt1)

mltxt2 = '''
I'm a another multi-line string.
I can use single quotes because I only exist between two pairs of three consequtive quotes.
'''
print(mltxt2)

# Basic use of f-strings
a = 'foo'
b = 3
print('my var is a=', a, 'and also b=', b, '.')
# print('my var is a=' + a + 'and also b=' + b + '.')
# print('my var is a=' + a + ' and also b=' + str(b) + '.')
# print(f'my var is {a}, and also b={b}.')
# print(f"""Multiline strings can also be formatted.
# Here for example a = '{a}' and b = {b}.
# Hooray!
# """)

# Number formatting
a = 30 # int
print(f'a = {a:04d}')

b = 1.337 # float
print(f'b = {b:0.2f}')
print(f'b = {b:0.5f}')

pi = 3.1415926535897932384626433 # another float
print(f'π = {pi:0.10f}...')

x = 64321277
print(f'x = {x:e}') # scientific
print(f'x = {x:x}') # hexadecimal

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

def func(x, y, z=10):
    return x**2-2*y+z
print(func(1, 1))
# print(func(1, 1, 1))
# print(func(z=2))

def no_return(a):
    print(f'You entered "{a}"')
no_return(4)

# ----- Classes ----- #
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.initials = f'{first_name[0]}.{last_name[0]}.'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

p = Person('Danny', 'Mendel')
print(p, p.initials)

class Employee(Person):
    def __init__(self, first_name, last_name, company):
        super().__init__(first_name, last_name)
        self.company = company

    def __str__(self):
        return super().__str__() + f' works at {self.company}'

e = Employee('Jane', 'Doe', 'exocad')
print(e)

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
