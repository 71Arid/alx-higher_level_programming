#!/usr/bin/python3
""" joined """
import MySQLdb
import sys
if __name__ == '__main__':
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    stn = sys.argv[4]
    db = MySQLdb.connect(host=host, user=user, port=3306, passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT cities.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id ", (stn,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    cities_str = ', '.join(cities)
    print(cities_str)
    cur.close()
    db.close()
