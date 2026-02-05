#!/usr/bin/python3
"""
Module 8-rectangle
"""


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """ Docstring for area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Docstring for integer_validator """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ Docstring for init

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
