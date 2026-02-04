#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    def print_sorted(self):
        """print list"""
        self.sort()
        print(self)
