"""Exercises with simple functions"""
from math import sqrt

def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    'TEST ME!'
    """
    return "TEST ME!"
    ...

a=10
def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    'TEST ME'
    """
    c=10
    return "TEST ME"
    ...


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    'TEST ME'
    """
    if len(x)>len(y):
        longest=x
    elif len(y)>len(x):
        longest=y
    else:
        longest="Equal in length"
    
    return "TEST ME"
    ...


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    'TEST ME'
    """
    x1, y1 = p1
    x2, y2 = p2
    k=sqrt((x2-x1)^2 + (y2-y1)^2)

    return "TEST ME"
    ...
