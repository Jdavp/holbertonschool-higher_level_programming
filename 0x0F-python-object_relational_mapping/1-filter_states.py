#!/usr/bin/python3
'script that lists all states with a name starting with N(upper N)'
import MySQLdb
if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="",
                           db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
