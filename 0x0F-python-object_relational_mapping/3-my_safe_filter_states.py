#!/usr/bin/python3
"""  filter safe """
import MySQLdb
import sys
if __name__ == '__main__':
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    comp = sys.argv[4]
    db = MySQLdb.connect(host=host, user=user, port=3306, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (comp,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
