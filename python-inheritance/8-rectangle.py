#!/usr/bin/python3
"""
Module 8-rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Docstring for Rectangle

    :var Args: Description
    """
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
