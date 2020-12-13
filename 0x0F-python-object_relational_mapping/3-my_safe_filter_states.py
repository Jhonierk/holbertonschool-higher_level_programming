#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) < 5:
        print(
            'Usage: {} username password database state_name'.format(argv[0]))
        exit(1)
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state = argv[4]
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    sql = cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        if (state == row[1]):
            print(row)
