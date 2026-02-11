#!/usr/bin/python3
"""
Docstring save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Fonction serve a  writes an Object to a text file,
    using a JSON representation:
    """
    with open('my_list.json', 'w') as json_file:
        json.dump(my_obj, json_file)
