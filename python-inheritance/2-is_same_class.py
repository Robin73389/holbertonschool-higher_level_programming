#!/usr/bin/python3
"""Class allow the check if
object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """return the instance"""

    if type(obj) is a_class:
        return True
    else:
        return False
