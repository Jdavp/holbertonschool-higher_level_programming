#!/usr/bin/python3
'script that takes in an argument and displays all values that matches the argument'
import MySQLdb
from sys import argv
if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="",
                           db="hbtn_0e_4_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
    FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = %s ORDER BY\
    cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    lista = []
    for row in query_rows:
        lista.append(row[0])
    print(", ".join(lista))
    cur.close()
    conn.close()
