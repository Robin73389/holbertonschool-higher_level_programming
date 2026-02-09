#!/usr/bin/python3

"""
Docstring for my fonction write_file
"""


def write_file(filename="", text=""):
    """
    Docstring: This fonction allows of create a file if the file already exists
    and delete the file if he exist
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
