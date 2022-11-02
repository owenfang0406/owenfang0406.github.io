from crypt import methods
from datetime import timedelta
from distutils.log import info
from turtle import update
from unittest import result
from flask import jsonify, make_response, redirect, Flask, request, render_template, session, url_for
import mysql.connector
import re, json
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Ppp0935082190",
    database = "website"
)
myCursor = db.cursor()

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "dei2jdoidj3209u54385897((*&*jid"
app.permanent_session_lifetime = timedelta(minutes=5)

def doJSON(tuple):
    dataDict= dict()
    dataDict['data']= dict()
    if tuple != None:
        dataDict['data']={'id':tuple[0],'name':tuple[1],'username':tuple[2]}
        infoJSON = json.dumps(dataDict, indent=5,ensure_ascii=False)
        return infoJSON
    elif tuple == None:
        dataDict['data'] = None
        infoJSON = json.dumps(dataDict, indent=5,ensure_ascii=False)
        return infoJSON



        


    

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
            IDsql =  """
            select id, name, username from member where username = %s
            """
            idArgs = (uname,)
            myCursor.execute(IDsql,idArgs)
            userInfo = myCursor.fetchone()
            infoJSON = doJSON(userInfo)
            uname = request.form["uname"]
            session["loggedin"] = True
            session["username"] = uname
            return redirect("/member")

@app.route("/member")
def ismember():
    if "username" and "loggedin" in session:
        user = session["username"]
        # queryContentSQL = """
        # select member.username, message.content from message
        # inner join member
        # on message.member_id = member.id
        # """
        # myCursor.execute(queryContentSQL)
        # content = myCursor.fetchall()
        return render_template("/member.htm", user = user, greeting="歡迎光臨，這是會員頁", message = "，歡迎登入系統")
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
        updateContentSQL = """
        insert into message(member_id, content)
        values (%s, %s)
        """
        myCursor.execute(updateContentSQL,updateContent)
        return redirect("/member")

    else:
        return redirect(url_for("ismember"))

@app.route("/api/member", methods = ["GET","PATCH"])
def loopUpMemberAPI():
    if "username" and "loggedin" in session:
        uname =request.args.get('username')
        if request.method == 'GET':
            if uname != "":
                IDsql =  """
                select id, name, username from member where username = %s
                """
                idArgs = (uname,)
                myCursor.execute(IDsql,idArgs)
                userInfo = myCursor.fetchone()
                if userInfo:
                    infoJSON = doJSON(userInfo)
                    return infoJSON
                else: 
                    userInfo = doJSON(userInfo)
                    return userInfo
            else:
                return "please input username for query"
        elif request.method == 'PATCH':
            if "username" and "loggedin" in session:
                newname = request.json['name']
                name = session['username']
                updateSQL = """
                update member
                set name = %s
                where name = %s
                """
                updateArgs = (newname, name)
                myCursor.execute(updateSQL,updateArgs)
                db.commit()
                session.pop("username", None)
                session['username'] = newname
                return make_response(jsonify(
                    {
                        'ok':'true'
                    }
                ))
            else: 
                return make_response(jsonify(
                    {
                        'error':'true'
                    }
                ))

        else:
            return
    else: 
        userInfo = doJSON(None)
        return userInfo


if __name__ == '__main__':
    app.run(port=3000, debug=True)
