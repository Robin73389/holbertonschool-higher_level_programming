#!/usr/bin/python3
"""Module that adds two integers.
Only integers and floats are allowed.
Floats are cast to integers.
Raises TypeError on invalid input.
Returns the addition result."""


def add_integer(a, b=98):
    """Return the addition of two integers.
    Floats are cast to integers.
    Raises TypeError on invalid input."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    result = int(a) + int(b)

    return result
