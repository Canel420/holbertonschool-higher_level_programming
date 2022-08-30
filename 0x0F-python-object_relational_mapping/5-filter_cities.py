#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
5-filter_cities.py module

Script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE state_id=\
                (SELECT id FROM states WHERE name LIKE BINARY %s)\
                ORDER BY cities.state_id;", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
