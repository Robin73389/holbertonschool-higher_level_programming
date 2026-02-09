#!/usr/bin/python3
"""
Docsstrinf for fonction append_write
"""


def append_write(filename="", text=""):
    """
    Docstring wich of add new line in the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
