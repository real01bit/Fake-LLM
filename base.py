import sqlite3
import random

c2i = {}
i2c = []
siz = 0


def load_charset():
    global siz
    with open("charset.txt", "r", encoding="utf-8") as fp:
        s = fp.read()
        for c in s:
            c2i[c] = len(i2c)
            i2c.append(c)
    siz = len(i2c)


load_charset()


def base_input(con: sqlite3.Connection, p, k, commit=True):
    cur = con.cursor()
    cur.execute(
        "SELECT v FROM graph3 WHERE p0=? AND p1=? AND p2=? AND p3=?",
        p[:4],
    )
    r = cur.fetchone()
    if r is None:
        if p[0] == -1:
            r = 600
        else:
            r = 1
        cur.execute(
            "INSERT INTO graph3 values(?,?,?,?,?)",
            (p[0], p[1], p[2], p[3], r + k),
        )
        if commit:
            con.commit()
        return
    cur.execute(
        "UPDATE graph3 SET v=? WHERE p0=? AND p1=? AND p2=? AND p3=?",
        (r[0] + k, p[0], p[1], p[2], p[3]),
    )
    if commit:
        con.commit()


def base_output(con: sqlite3.Connection, p):
    cur = con.cursor()
    cur.execute(
        "SELECT p0,v FROM graph3 WHERE p1=? AND p2=? AND p3=?",
        p[:3],
    )
    res = cur.fetchall()
    cur.close()
    tmp = {}
    for it in res:
        tmp[it[0]] = it[1]
    counts = []
    for i in range(-1, siz):
        r = 1
        if i == -1:
            r = 600
        counts.append(tmp.get(i, r))
    return random.sample(range(-1, siz), k=1, counts=counts)[0]


if __name__ == "__main__":
    print(siz)
