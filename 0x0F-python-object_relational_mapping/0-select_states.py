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

    database = MYSQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                                database=argv[3], port=3306)
    database.execute("SELECT * FROM states ORDER BY states.id;")
    table = database.fetchall()
    for row in table:
        print(row)
