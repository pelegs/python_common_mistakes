from memory_profiler import profile
from numpy.random import uniform
from sys import argv

@profile
def sqr_list(nums):
    sqrs = []
    for n in nums:
        sqrs.append(n**2)
    return sqrs

@profile
def sqr_gen(nums):
    for n in nums:
        yield n**2

numbers = uniform(size=10000)
if argv[1] == 'list':
    for x in sqr_list(numbers):
        pass
elif argv[1] == 'gen':
    for x in sqr_gen(numbers):
        pass
else:
    raise ValueError(f"Uknown option '{argv[1]}'")
