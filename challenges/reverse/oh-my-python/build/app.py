from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return send_file("ohmy.pyc")

if (__name__ == "__main__"):
    app.run("0.0.0.0", 80, debug=False)
