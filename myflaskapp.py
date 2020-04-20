# https://mde.tw/cd2020 協同設計專案
# coding: utf-8
from flask import Flask, send_from_directory, request, redirect, \
                render_template, session, make_response, \
                url_for, abort, flash, g, jsonify
import random
# for random grouping
import requests
# for authomatic
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic

# from config.py 導入 CONFIG
from config import CONFIG

# for _curdir
import os

# for login_required decorator
from functools import wraps

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T', report_errors=False)

# 確定程式檔案所在目錄, 在 Windows 有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))

app = Flask(__name__)

# 使用 session 必須要設定 secret_key
# In order to use sessions you have to set a secret key
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T'

def __init__():
    # create required directory
    if not os.path.isdir(_curdir+"db"):
        try:
            os.makedirs(_curdir+"db")
        except:
            print("db mkdir error")
    # create SQLite database file if not existed
    try:
        conn = sqlite3.connect(_curdir+"db/database.db")
        cur = conn.cursor()
        # create table
        cur.execute("CREATE TABLE IF NOT EXISTS grouping( \
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                user TEXT not null, \
                date TEXT not null, \
                result TEXT not null, \
                memo TEXT);")
        cur.close()
        conn.close()
    except:
        print("can not create db and table")
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql' , mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    g.es("do nothing")
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'login' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('index'))

    return wrap
@app.route('/drawROC')
@login_required
def drawROC():
    return render_template("drawROC.html")
    
@app.route("/menu")
@login_required
def menu():
    menuList = ["guess", "drawROC", "randomgrouping"]
    return render_template("menu.html", menuList=menuList)
# setup static directory
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
@app.route("/guess")
@login_required
def guess():
    '''
    if not session.get('login'):
        return redirect(url_for('index'))
    '''
    # This is the starting form for guessing numbers game, mainly to generate answers, and to reset count to zero
    # Store answers of guessing
    theanswer = random.randint(1, 100)
    thecount = 0
    # Store the answer and the number of calculation variables in the session
    session['answer'] = theanswer
    session['count'] = thecount
    user = session.get('user')

    return render_template("guess.html", answer=theanswer, count=thecount, user=user)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)
@app.route('/req1')
def req1():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
@app.route('/red')
def red():
    # redirect to google
    return redirect("http://www.google.com")
@login_required
@app.route('/guessform')
def guessform():
    session["count"] += 1
    guess = session.get("guess")
    theanswer = session.get("answer")
    count = session.get("count")
    return render_template("guessform.html", guess=guess, answer=theanswer, count=count)
@app.route('/docheck', methods=['POST'])
def docheck():
    if not session.get('login'):
        return redirect(url_for('index'))
    # use session[] to save data
    # use session.get() to get session data
    # use request.form[] to get field data of form and send to template
    guess = request.form["guess"]
    session["guess"] = guess
    # if use execute doCheck directly, send it back to the root method
    if guess is None:
        redirect("/")
    # get answer from session, when execute doCheck directly, no session data will be accessed
    try:
        theanswer = int(session.get('answer'))
    except:
        redirect("/")
    # the data type from web based form is string
    try:
        theguess = int(guess)
    except:
        return redirect("/guessform")
    # every doCheck being executed increase the count session value
    session["count"] += 1
    count = session.get("count")
    # compare the answer and the guess value
    if theanswer < theguess:
        return render_template("toobig.html", guess=guess, answer=theanswer, count=count)
    elif theanswer > theguess:
        return render_template("toosmall.html", guess=guess, answer=theanswer, count=count)
    else:
        # 
        # got the answer, get count from session
        thecount = session.get('count')
        return "Guess "+str(thecount)+" times, finally got the answer, the answer is "+str(theanswer)+": <a href='/guess'>Play again</a>"
    return render_template("docheck.html", guess=guess)
 
@app.route("/randomgrouping")
@login_required
def randomGrouping():
    # url to get the student number data
    target_url = "http://mde.tw/cd2020/downloads/2020spring_cd_2a_list.txt"
    # use requests to retrieve data from url
    f = requests.get(target_url)
    # get student list from target_url
    # use splitlines() to put student number into studList
    studList = f.text.splitlines()
    # minimum number for each group
    num_in_one_group = 10
    # temp list to save the student number for each group
    gpList = []
    # whole class list
    group = []
    # number of member list for each group
    numList = []
    # get numList
    numList = getNumList(len(studList), num_in_one_group)
    # check numList
    # list numList
    #print("Expected number of member list:" + str(numList))
    
    output = ""
    gth = 1
    inc = 0
    
    # use shuffle method of random module to shuffle studList
    random.shuffle(studList)
    output += "Before sort: <br />"
    for i in numList:
        # print 20 * sign
        output += '=' * 20 + "<br />";
        output += "group " + str(gth) + " has " + str(i) + " members:<br />"
        # reset group list
        gpList = []
        for j in range(i):
            output += studList[j+inc] + "<br />"
            # append student number into grpList
            gpList.append(studList[j+inc])

        gth = gth + 1
        inc = inc + j
        # sort gpList
        gpList.sort()
        group.append(gpList)

    # print output which is the result before sorting
    print(output)
    # print group whis is the sorted result
    print("Sorted result:" + str(group))

    output = ""
    # output sorted result
    output += '=' * 20 + "<br />"
    output += 'Sorted result:<br />'
    gth = 1

    # list sorted data seperated by \n
    for i in range(len(group)):
        # print seperated mark
        output += '=' * 20 + "<br />"
        output += "group" + str(gth) + "<br />"
        gpList = []

        for j in range(len(group[i])):
            output += str(group[i][j]) + "<br />"

        gth = gth + 1

    print(output)
    return output
# get the distributed list among each group
def getNumList(total, eachGrp=10):
    # total is the number of students
    # each group at least 10 students
    #eachGrp = 10;
    # may divide into "grpNum" number of group
    grpNum = total // eachGrp;
    # check grpNum
    #print(grpNum)
    # vacan list
    splits = []
    # find remainder when total number divid into "grpNum" number of group
    remainder = total % grpNum
    # number of people in one group by calculation
    calGrp = total // grpNum

    for i in range(grpNum):
        splits.append(calGrp)

    # check first splits
    #print(splits)

    for i in range(remainder):
        splits[i] += 1

    # check final splits
    #print(splits);
    return splits;
@app.route('/')
@login_required
def index():
    return render_template('index.html')
@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)
    
    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
        
        # use session to save login user's email (試著將 @ 換為 _at_)
        #session['loginEmail'] = result.user.email.replace('@', '_at_')
        loginUser = result.user.email.split("@")[0]
        session["user"] = loginUser
        session["login"] = True
        
        CALLBACK_URL = "https://localhost:8443/autho_login"
    
        # The rest happens inside the template.
        return render_template('login.html', result=result, CALLBACK_URL=CALLBACK_URL)
    
    # Don't forget to return the response.
    return response
@app.route('/logout')
def logout():
    session.pop('login' , None)
    session.pop('user', None)
    flash('Logged out!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()

