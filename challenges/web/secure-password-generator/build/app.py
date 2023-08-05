from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import string
import random

app = Flask(__name__,template_folder="templates")
conn = sqlite3.connect('sql.db',check_same_thread=False)
cursor = conn.cursor()

def GenPassword(length):
    chars = ""
    special_chars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    for i in range(length):
        chars += random.choice(special_chars)
    for j in range(30-length):
        chars += random.choice(string.ascii_letters)
    return chars

@app.route('/')
def index():
    return redirect(url_for("randomPassword"))

@app.route('/randomPassword')
def randomPassword():

    level = request.args.get("level")
    if level != None and level != "":
        try:
            result = cursor.execute(f"select level from levels where levelname='{level}'")
            result = result.fetchone()
            result = result[0]

        except:
            result = 8
        if not isinstance(result,int) or result < 1 or result > 8:
            result = 8
        password = GenPassword(result-1)
        if level in ["Baby","Trivial","Easy","Normal","Medium","Hard","Expert","Insane"]:
            return render_template("password.html",level=level,Password=password)
        else:
            return render_template("password.html",level="🤡🤡🤡🤡🤡",Password=password)
    else:
        return render_template("password.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=False)
