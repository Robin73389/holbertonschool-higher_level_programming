#!/usr/bin/python3

"""
Docstring for Read_file
"""


def read_file(filename=""):
    """
    This function watch how read a file
    """
    with open("my_file_0.txt") as f:
        line = f.read()
        print(line)
