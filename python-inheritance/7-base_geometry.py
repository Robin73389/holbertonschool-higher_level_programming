#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """return Exception message"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} be greater than 0")
