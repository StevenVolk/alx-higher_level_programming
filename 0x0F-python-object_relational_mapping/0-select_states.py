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
            database=argv[3], port=3306) as database:
        database.execute("SELECT * FROM states ORDER BY id;")
        table = database.fetchall()
        for row in table:
            print(row)
