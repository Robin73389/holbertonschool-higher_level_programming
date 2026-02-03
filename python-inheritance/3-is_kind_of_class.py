#!/usr/bin/python3
"""Function allow if the object is exactly an instance of the specified class
"""


def is_kind_of_class(obj, a_class):
    """return object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
