#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    return Exception message
    """

    def area(self):
        """
        Area methode
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Methode integer
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Return Rectangle which return the methode
    """

    def __init__(self, width, height):
        """
        Methode init
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
