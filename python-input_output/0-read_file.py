#!/usr/bin/python3

"""
Docstring for Read_file
"""


def read_file(filename=""):
    """
    This function watch how read a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
