#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    """Print list"""

    def print_sorted(self):
        self.sort()
        print(self)
