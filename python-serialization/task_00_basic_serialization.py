#!/usr/bin/python3
"""
Docstring for python-serialization.task_00_basic_serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Docstring for serialize_and_save_to_file

    :param data: Description
    :param filename: Description
    """
    file_jason = json.dumps(data)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(file_jason)


def load_and_deserialize(filename):
    """
    Docstring for load_and_deserialize

    :param filename: Description
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
