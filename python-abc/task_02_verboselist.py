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
         print("Added [{}] to the list.".format(item))
         super().append(item)
       
    def extend(self, item):
        print("Extended the list with [{}] items.".format(len(item)))
        super().extend(item)
    
    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        print("Popped [{:d}] from the list.".format(self[index]))
        super().pop(index)

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)