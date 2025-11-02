import ptext
import random
import sqlite3

con = sqlite3.connect("graph.db")
pre = [-1, -1, -1, -1]
while True:
    try:
        # sentence = input("<human> ")
        # pre = ptext.text_input(sentence, 600000)
        pre = [-1, -1, -1, -1]
        print(f"<robot> {ptext.text_output(con, pre, 500)}")
    except Exception as e:
        # logging.error(str(e))
        raise e
