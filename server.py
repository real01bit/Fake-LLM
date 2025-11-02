import ptext
import random
from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route("/api", methods=("POST",))
def api_talk():
    ins = request.form["input"]
    len = int(request.form["length"])
    con = sqlite3.connect("graph.db")
    pre = ptext.text_input(con, ins, random.randint(2000000, 10000000))
    res = ptext.text_output(con, pre, len)
    return jsonify({"output": res})


@app.route("/")
def talk():
    return render_template("talk.html")


app.run("0.0.0.0", 11831, debug=False)
