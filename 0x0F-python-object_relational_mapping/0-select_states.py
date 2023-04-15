#!/usr/bin/python3
"""This module connects to a locally hosted mysql server using MySQLdb
    username, password and database name is passed to the terminal in order"""

import sys
import MySQLdb


if __name__ == '__main__':
    """module main function"""
    uname = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]
    try:
        db = MySQLdb.connect(host='localhost',
                             user=uname,
                             passwd=pwd,
                             db=dbname, port=3306)
        cur = db.cursor()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(e))
        exit(1)

    try:
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(e))
        cur.close()
        db.close()
        exit(1)

    for item in rows:
        print(item)

    cur.close()
    db.close()
