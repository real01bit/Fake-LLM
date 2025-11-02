import ptext
import sqlite3

con = sqlite3.connect("graph.db")

with open("text.txt", "r", encoding="utf-8") as fp:
    ptext.text_input_with_log(con, fp.read(), 60000000, commit=False)
    con.commit()

con.close()
