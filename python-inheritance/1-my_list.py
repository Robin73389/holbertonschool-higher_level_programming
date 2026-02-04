#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    """Print list"""

    def print_sorted(self):
        print(sorted(self))
