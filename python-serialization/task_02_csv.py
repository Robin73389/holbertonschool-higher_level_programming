#!/usr/bin/python3
"""
Docstring for python-serialization.task_02_csv
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Docstring for convert_csv_to_json

    :param csv_filename: Description
    """
    try:
        data = []

        with open(csv_filename, mode='r', newline='', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)
            for ligne in lecteur:
                data.append(ligne)

        with open("data.json", 'w', encoding='utf-8') as f:
            json.dump(data, f)

        return True

    except FileNotFoundError:
        return False
