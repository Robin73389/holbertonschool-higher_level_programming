#!/usr/bin/python3
"""
Docstring Student
"""


class Student:
    """
    Docstring for Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Docstring for __init__

        :param self: Description
        :param first_name: Description
        :param last_name: Description
        :param age: Description
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Docstring for to_json

        :param self: Description
        :param attrs: Description
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)}
        else:
            return self.__dict__.copy()
