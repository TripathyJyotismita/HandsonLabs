"""Fibonacci sequences using generators
"""

__author__ = "Jyotismita Tripathy"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2020/08/09 $"

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

for n in fibonacci(1000):
    print(n)
