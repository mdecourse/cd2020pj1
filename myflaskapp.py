# https://mde.tw/cd2020 協同設計專案
# coding: utf-8
from flask import Flask, send_from_directory, request, redirect, render_template, session
import random
# for random grouping
import requests

app = Flask(__name__)

# 使用 session 必須要設定 secret_key
# In order to use sessions you have to set a secret key
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T'

# setup static directory
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
@app.route("/")
def index():
    # This is the starting form for guessing numbers game, mainly to generate answers, and to reset count to zero
    # Store answers of guessing
    theanswer = random.randint(1, 100)
    thecount = 0
    # Store the answer and the number of calculation variables in the session
    session['answer'] = theanswer
    session['count'] = thecount

    return render_template("index.html", answer=theanswer, count=thecount)


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
@app.route('/guessform')
def guessform():
    session["count"] += 1
    guess = session.get("guess")
    theanswer = session.get("answer")
    count = session.get("count")
    return render_template("guessform.html", guess=guess, answer=theanswer, count=count)
@app.route('/docheck', methods=['POST'])
def docheck():
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
        return "Guess "+str(thecount)+" times, finally got the answer, the answer is "+str(theanswer)+": <a href='/'>Play again</a>"
    return render_template("docheck.html", guess=guess)
 
@app.route("/randomgrouping")
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

if __name__ == "__main__":
    app.run()

