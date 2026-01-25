#!/usr/bin/python3
"""Module that contains the say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first_name> <last_name>.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.
            Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
