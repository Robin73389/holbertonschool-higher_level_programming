#!/usr/bin/python3
"""Class Abstréte"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Class Animal"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class Dog"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Class Cat"""

    def sound(self):
        return "Meow"
