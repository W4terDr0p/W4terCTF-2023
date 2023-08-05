from flask import Flask, render_template, request
import sqlite3
import os


app = Flask(__name__,template_folder="templates")

conn = sqlite3.connect('sql.db', check_same_thread=False)
cursor = conn.cursor() 

def waf(str):
    length = 0
    for c in str:
        if(c.isdigit()):
            length += length * 10 + int(c)
    return length > 0 and length < 10

@app.route('/')
def index():
    return render_template('index.html',hint="小 GZ 露出 flag 的一角，但是这离成功远远不够，你能将 flag 整条拖出来吗")

@app.route('/hint')
def hint():
    return render_template('hint.html')

@app.route('/getFlag')
def getFlag():
    flag_len = request.args.get("len")

    try:
        if(waf(flag_len)):
            result = cursor.execute(f"select substr(flag,1,{flag_len}) from flag")
            result = result.fetchone()
            print(len(result[0]))
            if(len(result[0])):
                return render_template('getflag.html',message=result[0]) # Only the first query information of sql can be obtained
            else:
                return render_template('getflag.html',message="nothing here")
        else:
            return render_template('getflag.html',message="len should be 0 < len < 10")
    except:
        return render_template('getflag.html',message="Error! Please Try Again Meow~ ")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=False)