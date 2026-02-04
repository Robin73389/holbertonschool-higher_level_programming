#!/usr/bin/python3
"""
Module that provides a function to check if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """return obj if True"""
    return type(obj) is not a_class
    return isinstance(obj,a_class)


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
