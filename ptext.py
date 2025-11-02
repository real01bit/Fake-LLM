import base
import sqlite3


def text_input(con: sqlite3.Connection, s, k, end=False, ke=0, commit=True):
    p = [-1, -1, -1, -1]
    for c in s:
        p.pop()
        p.insert(0, base.c2i.get(c, 0))
        base.base_input(con, p, k)
    q = p.copy()
    if end:
        q.pop()
        q.insert(0, -1)
        base.base_input(con, q, ke, commit)
    return p


def text_input_with_log(con: sqlite3.Connection, s, k, end=False, ke=0, commit=True):
    p = [-1, -1, -1, -1]
    siz = len(s)
    tot = 0
    for c in s:
        p.pop()
        p.insert(0, base.c2i.get(c, 0))
        base.base_input(con, p, k, commit)
        tot += 1
        print(f"{tot}/{siz}", end="\r")
    q = p.copy()
    if end:
        q.pop()
        q.insert(0, -1)
        base.base_input(con, q, ke)
    return p


def text_output(con: sqlite3.Connection, p, l=10000):
    t = ""
    for i in range(l):
        r = base.base_output(con, p)
        p.pop()
        p.insert(0, r)
        if r == -1:
            return t
        t += base.i2c[r]
    return t
