#!/usr/bin/python3
'takes an argument and displays all values that matches the argument'
import MySQLdb
from sys import argv
if __name__ == '__main__':

    'make a list of all states'
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
