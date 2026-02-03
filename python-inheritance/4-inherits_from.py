#!/usr/bin/python3
"""
Module that provides a function to check if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class
        and not an instance of a_class itself, otherwise False.
    """
    if type(obj) is not a_class:
        return True
    else:
        return False
