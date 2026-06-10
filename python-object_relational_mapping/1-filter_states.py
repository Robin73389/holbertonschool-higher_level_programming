#!/usr/bin/python3
"""The program print the two last line to my database"""


import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
