#!/usr/bin/python3
"""
Module that provides a function to check if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """return obj if True"""

    return type(obj) is not a_class
