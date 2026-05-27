#!/usr/bin/python3
"""Serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Methode serialize

    Args:
        data
        filename
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """

    Args:
        filename

    Returns:
        DATA
    """
    with open(filename, "r", encoding='utf-8') as read:
        data = json.load(read)

    return data


if __name__ == "__main__":
    print()
