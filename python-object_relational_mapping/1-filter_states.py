#!/usr/bin/env python3
"""The program print the two last line to my database"""


import MySQLdb
import sys


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                           passwd="root",
                           db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows[-2:]:
        print(row)
    cur.close()
    conn.close()
