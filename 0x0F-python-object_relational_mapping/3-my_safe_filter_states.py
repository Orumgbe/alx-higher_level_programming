#!/usr/bin/python3
"""A little documentaTION"""

import sys
import MySQLdb

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(
                user=sys.argv[1], passwd=sys.argv[2],
                db=sys.argv[3],
                host='localhost',
                port=3306)

        cursor = db.cursor()
    except MySQL.Error as e:
        print("Error [{}]: {}".format(e[0], e[1]))

    try:
        cursor.execute("SELECT * FROM states WHERE name = '{}'\
                        ORDER BY id ASC".format(sys.argv[4]))
    except MySQL.Error as e:
        print("Error [{}]: {}".format(e[0], e[1]))

    states = cursor.fetchall()
    for state in states:
        print(state)
