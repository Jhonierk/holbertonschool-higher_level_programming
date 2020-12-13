#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) < 4:
        print(
            'Usage: {} username password database state_name'.format(argv[0]))
        exit(1)
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    sql = cursor.execute('''
                        SELECT cities.id, cities.name, states.name
                        FROM cities JOIN states
                        ON cities.state_id = states.id
                        ORDER BY cities.id ASC
                            ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
