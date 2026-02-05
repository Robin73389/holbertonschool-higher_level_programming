#!/usr/bin/python3

"""
Docstring for project abstractmethod
"""

from math import pi

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Class Shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Class Circle
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(self):
    """
    Docstring shape_info
    """
    print("Area: {}".format(self.area()))
    print("Perimeter: {}".format(self.perimeter()))
