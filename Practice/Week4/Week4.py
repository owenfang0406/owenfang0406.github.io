from crypt import methods
from flask import redirect, Flask, request, render_template

app = Flask(__name__, static_folder="public", static_url_path="/")

@app.route("/")
def index():
    return render_template("loginPage.htm", greeting = "歡迎光臨，請輸入帳號密碼")

@app.route("/signin", methods=["POST"])
def checkIDpsw():
    uname = request.form["uname"]
    psw = request.form["psw"]
    if uname != "" and psw != "":
        if uname == "test" and psw == "test":
            return redirect("/member")
        else:
            return redirect("/error?message=帳號、或密碼輸入錯誤")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")
@app.route("/error")
def displayErr():
    message = request.args["message"]
    return render_template("error.htm", greeting = "失敗頁面" , message = message)

@app.route("/member")
def ismember():
    return render_template("member.htm",greeting="歡迎光臨，這是會員頁", message = "恭喜您，成功登入系統")

app.run(port=3000)