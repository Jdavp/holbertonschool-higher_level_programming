#!/usr/bin/python3
'Write a script that lists all states from the database hbtn_0e_0_usa'
import MySQLdb
if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="",
                           db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()