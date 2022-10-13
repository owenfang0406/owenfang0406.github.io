from datetime import timedelta
from flask import redirect, Flask, request, render_template, session, url_for, g

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "374y9r8yfw1020ri23ir094r5qdixk"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def index():
    if "user" in session:
        return redirect("/member")
    else:
        return render_template("loginPage.htm", greeting = "歡迎光臨，請輸入帳號密碼")

@app.route("/signin", methods=["POST"])
def checkIDpsw():
    uname = request.form["uname"]
    psw = request.form["psw"]
    if uname != "" and psw != "":
        if uname == "test" and psw == "test":
            session["user"] = uname
            session.permanent = True
            return redirect("/member")
        else:
            return redirect("/error?message=帳號、或密碼輸入錯誤")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")
@app.route("/error")
def displayErr():
    message = request.args.get("message",default="")
    return render_template("error.htm", greeting = "失敗頁面" , message = message)

@app.route("/member")
def ismember():
    if "user" in session:
        return render_template("member.htm",greeting="歡迎光臨，這是會員頁", message = "恭喜您，成功登入系統")
    else:
        return redirect(url_for("index"))

@app.route("/signout")
def signout():
    session.pop("user", None)
    return redirect("/")

@app.route("/square/<number>")
def square(number):
    number = int(number)
    result = number * number
    return render_template("square.htm", greeting = "正整數平方計算結果", message = str(result))

app.run(port=3000)