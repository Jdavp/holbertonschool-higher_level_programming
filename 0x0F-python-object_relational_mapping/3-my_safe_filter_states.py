#!/usr/bin/python3
'takes an argument and displays all values that matches the argument'
import MySQLdb
from sys import argv
if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="",
                           db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BYNARY name = %s", (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
