#!/usr/bin/python3
"""
class Square wich check size
"""


class Square:

    """
    Docstring for Square
    """

    def __init__(self, size=0):
        self.__sizeof = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        return
