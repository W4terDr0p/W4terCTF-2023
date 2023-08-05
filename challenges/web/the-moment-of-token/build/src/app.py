from flask import Flask, render_template, request, make_response
import jwcrypto.jwt as jwt
import os, time
from base64 import b32encode

app = Flask(__name__)
key = jwt.JWK.generate(kty='oct', size=256)
flag = os.environ.get("GZCTF_FLAG")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html",
                           note=">>> Login to get your flag! <<<")


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    now = int(time.time())
    try:
        if now - int(password) > 5:
            return render_template("index.html",
                                   note=">>> You missed the moment! <<<")
        token = jwt.JWT(header={"alg": "HS256"},
                        claims={
                            "username": username,
                            "gift": b32encode(flag.encode()).decode()
                        })
        token.make_signed_token(key)
        token_cookie = token.serialize()
        res = make_response(
            render_template("index.html", note=">>> Login success! <<<"))
        res.set_cookie('token', token_cookie, httponly=True, max_age=1)
        return res
    except:
        return render_template("index.html", note=">>> Invalid password! <<<")


if (__name__ == "__main__"):
    app.run("0.0.0.0", 80, debug=False)
