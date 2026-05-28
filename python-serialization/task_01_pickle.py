#!/usr/bin/env python3
"""Serializz"""

import pickle


class CustomObject():
    """Class CustomObject"""
    def __init__(self, name, age, is_student):
        """_summary_

        Args:
            name(str)
            age (int):
            is_student (bool):
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Method display

            Args:
                self()
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Method serialize

            Args:
                self()
                filename
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)

        except IOError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Method serialize
            Args:
                cls()
                filename()
        """
        try:
            with open(filename, 'rb') as file:
                load = pickle.load(file)
                return load

        except (IOError, AttributeError):
            return None


if __name__ == "__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()
