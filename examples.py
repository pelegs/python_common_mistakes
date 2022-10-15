"""
Section ideas
1. loops
2. assignment
3. comprehensions
4. file handling
5. mutable types
6. string formatting
7. type checking
8. singleton (in)equalities
9. bool vs. length
10. dict items() function
11. Good libs to use: logging, argparse, itertools, etc.
12. NUMPY
13. if __name__ == '__main__'
"""
# ------------------------------------------------ #

#####################
# String formatting #
#####################

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
# print('my var is a=', a, 'and also b=', b, '.')
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

# Lists, dictionaries and functions
lst = [1,2,3,4,5]
print(f'l = {lst[2]}')

natlang = {
    'Peleg': 'Hebrew',
    'Aaron': 'English',
    'Emanuel': 'German'
}
print(f'Aaron\'s native language is {natlang["Aaron"]}.')
print(f"Emanuel's native language is {natlang['Emanuel']}.")

# Should I add left/right justification?..

# ------------------------------------------------ #

#######################
# Variable assignment #
#######################

# Multiple assignment
a, b, c, d = 10, 20, -50, 35
print(f'a={a}, b={b}, c={c}, d={d}')

# Expanding arrays using assignment
a, b, c = (-50, 20, 'test')
d, e = ['Hi', 'Hello']
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')

# Creating arrays by multiple assignment
a, *b = 10, 20, 30, 40, 50
print(f'a={a}, b={b}')

# Multiple equality
a = b = c = 0
print(f'a={a}, b={b}, c={c}')
a = -1
print(f'a={a}, b={b}, c={c}')

# Assigning values of truth statements
a = True and False
b = 1 < 5
c = a or b
print(f'a={a}, b={b}, c={c}')

# ------------------------------------------------ #

#######################
# Lists, tuples, sets #
#######################

# Lists
def somefunc():
    pass
lst = [1, 'a', True, 'cow', [0, 1, 2, 3], 2, somefunc, 5]
print(lst)
lst[2] = not(lst[2])
lst[-1] *= 3
del lst[-2]
print(lst)

# Tuples
tup = (1, 5, 'b', False, (0, 0, 0), [1, 1, 1])
print(tup)
# tup[1] += 5 # oops

# Sets
st = set([1, 2, 3, 1, 2, 1, 1, 3, 4, 5, 1, 2, 1, 1, 5])
print(st)
# st[1] = -3 # oops
st2 = set([True, (1,1,1), (1,1,1), None, (1,1,1,1), False, (1,1,1), (1,1,1,1), True, None, None])
print(st2)
# ------------------------------------------------ #

#############
# For loops #
#############

# Iterating over elemnts
arr = ['foo', 'bar', 'baz', 'bla', 'yo']
for i in range(len(arr)): # Don't do
    print(arr[i])

lst = ['foo', 'bar', 'baz', 'bla', 'yo']
for element in lst: # Better
    print(element)

# With enumeration
lst = ['foo', 'bar', 'baz', 'bla', 'yo']
for i, element in enumerate(lst):
    print(f'{i+1}: {element}')

# Iterating two or more lists

words_list = ['foo', 'bar', 'baz', 'bla', 'yo']
animals_list = ['Tapir', 'Dog', 'Cat', 'Turtle', 'Bear']
for i in range(len(words_list)): # Don't do
    print(words_list[i], animals_list[i])

# Index out of range
words_list = ['foo', 'bar', 'baz', 'bla', 'yo']
animals_list = ['Tapir', 'Dog', 'Cat', 'Turtle']
for i in range(len(words_list)): # Also don't do
    print(words_list[i], animals_list[i])

# Use zip() function
words_list = ['foo', 'bar', 'baz', 'bla', 'yo']
animals_list = ['Tapir', 'Dog', 'Cat', 'Turtle']
for word, animal in zip(words_list, animals_list): # Better
    print(word, animal)

# zip() with many lists
words_list = ['foo', 'bar', 'baz', 'bla', 'yo', 'aaa', 'ooo']
animals_list = ['Dog', 'Cat', 'Turtle', 'Rabbit', 'Bear', 'Tapir', 'Dolphin']
devops_list = ['Aaron', 'Alemseged', 'Emanuel', 'Frauke', 'Nehru', 'Peleg', 'Satya']
colors_list = ['Orange', 'Green', 'Blue', 'Purple', 'Pink', 'Red', 'White']
for word, animal, person, color in zip(words_list, animals_list, devops_list, colors_list):
    print(word, animal, person, color)

# Iterating over dictionaries
capitals = {
    'Germany': 'Berlin',
    'France': 'Paris',
    'Italy': 'Rome',
    'Canada': 'Ottawa',
    'Sweden': 'Stockholm',
    'The Netherlands': 'not the Hague',
}
# don't
# for country in capitals:
    # print(f'The capital of {country} is {capitals[country]}.')

# do
for country, city in capitals.items():
    print(f'The capital of {country} is {city}.')

# ------------------------------------------------ #

#################
# Type checking #
#################

# Not best practice
a = 3.1
if type(a) == float:
    print(f'{a} is a float')

# Better
b = 'text'
# b = ['text', 4]
if isinstance(b, str):
    print(f'"{b}" is a string')
else:
    print(f'{b} is not a string')

# Inheritence
# using type(x)==y might cause violation of Liskov substitution principle
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, -5)
print(type(p) == tuple)
print(isinstance(p, tuple))

# ------------------------------------------------ #

#################
# File handling #
#################

# Do NOT use open() and close() - instead use 'with'
with open('example.txt', 'r') as file:
    txt = file.read()
print(txt)

# Split lines directly into a list
with open('example.txt', 'r') as file:
    txt = file.readlines()
print(txt)

# Same for writing a file
txt = """
It was the dawn of the third age of mankind.
Ten years after the Earth Minbari war... the Babylon project was dream giving form.
It's goal to prevent another war by creating a place where humans and aliens could work out their differences peacefully.
It's a port of call, home away from home for diplomas, hustlers, entrepreneurs, and wanders.
Humans and aliens wrap in two million five hundred thousand tons of spinning metal, all alone in the night.
It can be a dangerous place, but it's our last best hope for peace.
This is the story of last of the Babylon stations.
The year is 2258 - the name of the place is Babylon 5.
"""
with open('output.txt', 'w') as file:
    file.write(txt)

# ------------------------------------------------ #

##################
# Comprehensions #
##################

# List comprehensions
xs = [1, 2, 3, 4, 5, 6, 7]
ys = [x**2 for x in xs]
print(ys)

# Nested loops inside comprehension
nums = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
lst = [(n, l) for n in nums for l in letters]
print(lst)

# 1-to-1 matching inside comprehension
nums = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
lst = [(n, l) for n, l in zip(nums, letters)]
print(lst)

# If conditionals in comprehensions
even_nums = [n for n in range(20) if n%2==0]
print(even_nums)

jumping_nums = [n if n%2==0 else -n for n in range(20)]
print(jumping_nums)

# More complex example
# This:
word_count = []
with open('example.txt', 'r') as file:
    txt = file.readlines()
for line in txt:
    word_count.append(len(line.split()))
print(f'Word count using the boring way: {word_count}')

# ...can be written succinctly as:
with open('example.txt', 'r') as file:
    word_count = [len(line.split()) for line in file.readlines()]
print(f'Word count using list comprehension: {word_count}')

# Dictionary comprehensions
devops_list = ['Aaron', 'Alemseged', 'Emanuel', 'Frauke', 'Nehru', 'Peleg', 'Satya']
colors_list = ['Orange', 'Green', 'Blue', 'Purple', 'Pink', 'Red', 'White']
devops_cols = {dev: col for dev, col in zip(devops_list, colors_list)}
print(devops_cols)

# A bit more complex?
# Create a dict which contains the first word of each line as key
# and the length of each line as value.
with open('example.txt', 'r') as file:
    lines_len = {
        line.split()[0]: len(line.split())
        for line in file.readlines()
    }
print(lines_len)

# ------------------------------------------------ #

#################
# main function #
#################

if __name__ == "__main__":
    print('yay?')
    # print(__name__)

# Example
import sys
sys.path.append(".")
import mylib as lib
print(lib.func(2))
