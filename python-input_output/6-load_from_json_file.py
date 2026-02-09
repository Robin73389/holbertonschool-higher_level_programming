#!/usr/bin/python3
"""
Docstring load_from_json_file
"""

import json


def load_from_json_file(filename):
    """
    This fonction  creates an Object from a "JSON file":
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
