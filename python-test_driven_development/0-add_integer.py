#!/usr/bin/python3
"""Module for function of adding integer"""


def add_integer(a, b=98):
    """Adding integers function"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
