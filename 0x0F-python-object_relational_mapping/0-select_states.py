#!/usr/bin/python3
"""

a script that lists all states from the database hbtn_0e_0_usa

"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """

    accessing database

    """

    with MYSQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
            db=argv[3], port=3306) as db:
        db.execute("SELECT * FROM states ORDER BY id ASC")
        table = db.fetchall()
        for row in table:
            print(row)
