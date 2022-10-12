from unittest import result
from flask import Flask 
from flask import request
import json
from flask import redirect
app = Flask(__name__)  #建立 Application 物件


@app.route("/getSum")
def getSum():
    maxNumber = request.args.get("max", 100)
    maxNumber = int(maxNumber)
    minNumber = request.args.get("min", 1)
    minNumber = int(minNumber)
    print("最大數字",maxNumber)
    result = 0
    for n in range(minNumber,maxNumber + 1):
        result += n
    return "結果" + str(result)
#建立路徑 / 對應得處理函式
@app.route("/en/")
def index_english():
    return json.dumps({
            "status": "ok",
            "text": "Hello World"
    }, ensure_ascii=False)


@app.route("/zh_tw/")
def index_chinese():
    return json.dumps({
        "status": "ok",
        "text": "你好，歡迎光臨"
    }, ensure_ascii=False)

@app.route("/")
def index():
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
        
    else:
        return redirect("/zh_tw/")
@app.route("/data")
def getData():
    return "My Data"

#動態路由：建立路經 /user/使用者名稱 對應函式

@app.route("/user/<ursername>")
def handleUser(username):
    if username == "Owen":
        return "你好 " + username
    else:
        return "hello " + username

app.run(port = 3000)

