#!/usr/bin/python3
"""
Docstring for python-abc.task_02_verboselist
"""
from abc import ABC, abstractmethod


class VerboseList(list):
    """
    Docstring for VerboseList
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        print("Popped [{d}] from the list.".format(self[index]))
        super().pop(index)
