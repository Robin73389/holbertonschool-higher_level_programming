#!/usr/bin/env python3
"""CSV to Json"""

import csv
import json


def convert_csv_to_json(CSV):
    """Method who convert CSV to Json

            Args:
                CSV
    """

    try:
        with open(CSV, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open(CSV, mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except IOError:
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
