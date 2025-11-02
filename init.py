import sqlite3

con = sqlite3.connect("graph.db")
cur = con.cursor()
cur.execute("CREATE TABLE graph3(p0,p1,p2,p3,v)")
