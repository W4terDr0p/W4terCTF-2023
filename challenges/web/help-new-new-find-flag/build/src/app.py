from flask import Flask, render_template, request
import os
import urllib.parse
import random

app = Flask(__name__)

blacklist = [
    "{", "%", "`", "#", "$", "&", "*", "+", "\'", "\"", ";", "|", "0x", "\\u",
    "\\x", "?", "[", "~", "env"
]
files = ["cold1.txt", "cold2.txt", "cold3.txt", "joke.txt"]
keys = [
    "/proc/sys/kernel/random/boot_id", "/etc/passwd",
    "/sys/class/net/eth0/address"
]


@app.route('/', methods=['GET'])
def greet():
    return render_template("index.html",
                           files=files,
                           content="",
                           mood="normal",
                           comment="你好，这里是奇怪 new new,快来和 new new 一起找flag吧")


@app.route('/find', methods=['POST'])
def view():
    file = urllib.parse.unquote(request.values.get('check'))
    checking = True
    try:
        for i in blacklist:
            if i in file:
                checking = False
                break
        if not checking:
            return render_template("index.html",
                                   files=files,
                                   content="你这是违法行为，走跟我去自首",
                                   mood="confused",
                                   comment="你传了什么奇奇怪怪的东西?")
        if not (os.path.exists(file) and os.path.isfile(file)):
            return render_template("index.html",
                                   files=files,
                                   content=str(file),
                                   mood="wordless",
                                   comment="emmm 你有在找flag吗")
        if "/flag" in file or "app.py" in file:
            raise PermissionError
        else:
            with open(file, 'r', encoding="utf-8") as f:
                content = f.read()
                f.close()
            if file in files:
                content = content.split("\n\n")
                content = random.choice(content)
            if file in keys:
                return render_template("index.html",
                                       content=content,
                                       files=files,
                                       mood="normal",
                                       comment="这里的东西会不会有什么用呢?")
            else:
                return render_template("index.html",
                                       content=content,
                                       files=files,
                                       mood="normal",
                                       comment="这里好像找不到flag呢")
    except Exception:
        raise PermissionError


if (__name__ == "__main__"):
    app.run("0.0.0.0", 80, debug=True)
