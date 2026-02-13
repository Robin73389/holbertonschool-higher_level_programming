#!/usr/bin/python3
"""
Docstring for python-serialization.task_01_pickle
"""
import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param age: Description
        :param is_student: Description
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Docstring for display
        :param self: Description
        """
        print("Name: {:s}".format(self.name))
        print("Age: {:d}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Docstring for serialize
        :param self: Description
        :param filename: Description
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Docstring for deserialize

        :param cls: Description
        :param filename: Description
        """
        with open(filename, 'rb') as f1:
            return pickle.load(f1)
