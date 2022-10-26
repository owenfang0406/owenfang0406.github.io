from datetime import timedelta
from os import uname
from unicodedata import name
from flask import redirect, Flask, request, render_template, session, url_for
import mysql.connector
import re
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "website"
)
myCursor = db.cursor()

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "dei2jdoidj3209u54385897((*&*jid"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def index():
    if "username" in session:
        return redirect("/member")
    else:
        return render_template("loginPage.htm", greeting ="歡迎光臨，請註冊登入系統")

@app.route("/signin", methods=["POST"])
def checkIDpsw():
    msg = ''
    if request.method == 'POST' and 'uname' in request.form and 'psw' in request.form:
        uname = request.form["uname"]
        psw = request.form["psw"]
        QueryCd = """
        select * from member 
        where username = %s and password = %s
        """
        QueryInput = (uname, psw)
        myCursor.execute(QueryCd, QueryInput)
        account = myCursor.fetchone()
        if account:
            session["loggedin"] = True
            session["username"] = account[1]
            session.permanent = True
            msg = "登入成功"
            return redirect(url_for("ismember"))
        else:
            return redirect("/error?message=帳號或密碼輸入錯誤")
            
    # if uname != "" and psw != "":
    #     if uname == "test" and psw == "test":
    #         session["user"] = uname
    #         session.permanent = True
    #         return redirect("/member")
    #     else:
    #         return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/error")
def displayErr():
    message = request.args.get("message", default="")
    return render_template("error.htm", greeting = "失敗頁面", message = message)

@app.route("/signup", methods=["POST"])
def signUp():
    msg = ''
    if request.method == 'POST' and 'uname' in request.form and 'psw' in request.form:
        name = request.form["name"]
        uname = request.form["uname"]
        psw = request.form["psw"]
        checkIfDuplicate = """
        select * from member where username = %s
        """
        checkInput = (uname,)
        myCursor.execute(checkIfDuplicate,checkInput)
        account = myCursor.fetchone()
        if account:
            return redirect("/error?message=帳號已經被註冊")
        elif not re.match(r'^[a-zA-Z0-9_]*$', uname):
            return redirect("/error?message=錯誤！帳號含有特殊字元")
        elif not name or not uname or not psw:
            return redirect("/error?message=註冊表單未完全填寫，請重新操作！")
        else:
            insertionCd = """insert into member(name, username, password)values(%s,%s,%s)"""
            inputInsertion = (name, uname, psw)
            myCursor.execute(insertionCd,inputInsertion)
            db.commit()
            uname = request.form["uname"]
            session["loggedin"] = True
            session["username"] = uname
            return redirect("/member")

@app.route("/member")
def ismember():
    if "username" and "loggedin" in session:
        user = session["username"]
        queryContentSQL = """
        select member.username, message.content from message
        inner join member
        on message.member_id = member.id
        """
        myCursor.execute(queryContentSQL)
        content = myCursor.fetchall()
        return render_template("/member.htm", user = user, greeting="歡迎光臨，這是會員頁", message = "，歡迎登入系統", content = content)
    else:
        return redirect(url_for("index"))

@app.route("/signout")
def signout():
    session.pop("username", None)
    session.pop("loggedin", None)
    session.pop("_permanent", None)
    return redirect("/")

@app.route("/pushContents", methods = ["POST"])
def pushContents():
    content = request.form["msg"]
    uname = session["username"]
    queryCondition = (uname,)
    myCursor = db.cursor(buffered=True)
    queryUserID = """
    select id from member where name = %s
    """
    myCursor.execute(queryUserID,queryCondition)
    member_id = myCursor.fetchone()
    if content != "":
        updateContent = (member_id[0], content,)
        print(updateContent)
        updateContentSQL = """
        insert into message(member_id, content)
        values (%s, %s)
        """
        myCursor.execute(updateContentSQL,updateContent)
        return redirect("/member")

    else:
        return redirect(url_for("ismember"))

app.run(port=3000)