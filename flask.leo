<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2"/>
<globals/>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="amd.20150311165615.4"><vh>@settings</vh>
<v t="amd.20150311165615.5"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="amd.20150311165615.6"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="amd.20150313083555.45"><vh>About cd2020pj1</vh></v>
<v t="leo.20200311103136.1"><vh>generate self-signed certificate</vh></v>
<v t="leo.20200409150450.1"><vh>random grouping</vh></v>
<v t="leo.20200311104947.1"><vh>use pybean.py to connect to SQLite</vh></v>
<v t="leo.20200311104223.1"><vh>use peewee to connect to SQLite</vh></v>
<v t="amd.20150311165615.9"><vh>@path ./</vh>
<v t="amd.20151020231829.1"><vh>@edit .gitignore</vh></v>
<v t="leo.20200311090825.1"><vh>@edit README.md</vh></v>
<v t="amd.20150311165615.30"><vh>@edit wsgi.py</vh></v>
<v t="amd.20150311165615.31"><vh>@clean myflaskapp.py</vh>
<v t="amd.20151020232112.1"><vh>send_static</vh></v>
<v t="amd.20151020232140.1"><vh>index</vh></v>
<v t="amd.20151020232703.1"><vh>user</vh></v>
<v t="amd.20151020232845.1"><vh>req1</vh></v>
<v t="amd.20151020233400.1"><vh>red</vh></v>
<v t="amd.20151021000403.1"><vh>guessform</vh></v>
<v t="amd.20151021000629.1"><vh>docheck</vh></v>
<v t="leo.20200409151441.1"><vh>randomGrouping</vh></v>
<v t="leo.20200409151603.1"><vh>getNumList</vh></v>
</v>
</v>
<v t="amd.20151020232503.1"><vh>@path static</vh></v>
<v t="amd.20151020234043.1"><vh>@path templates</vh>
<v t="amd.20151020234049.1"><vh>@edit index.html</vh></v>
<v t="amd.20151020234120.1"><vh>@edit user.html</vh></v>
<v t="amd.20151021000500.1"><vh>@edit guessform.html</vh></v>
<v t="amd.20151021000748.1"><vh>@edit docheck.html</vh></v>
<v t="amd.20151021083709.1"><vh>@edit toobig.html</vh></v>
<v t="amd.20151021083719.1"><vh>@edit toosmall.html</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="amd.20150311165615.31">@language python
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

@others

if __name__ == "__main__":
    app.run()

</t>
<t tx="amd.20150311165615.4"></t>
<t tx="amd.20150311165615.5">QSplitter::handle {
    background-color: #CAE1FF; /* lightSteelBlue1 */
}

QStackedWidget {
    /* background-color:lightpink; */
    border-color: red;
    padding: 0px;
    /* border-width: 0px; */
    /* background-color: yellow; */
}

QSplitter {
    border-color: white;
    background-color: white;
    border-style: solid;
}

QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="amd.20150311165615.6">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="amd.20150311165615.9"></t>
<t tx="amd.20150313083555.45">Application of Python and Flask on the colloaborative mechanical design.

Stared on March 11, 2020
</t>
<t tx="amd.20151020232112.1"># setup static directory
@app.route('/static/&lt;path:path&gt;')
def send_static(path):
    return send_from_directory('static', path)</t>
<t tx="amd.20151020232140.1">@app.route("/")
def index():
    # This is the starting form for guessing numbers game, mainly to generate answers, and to reset count to zero
    # Store answers of guessing
    theanswer = random.randint(1, 100)
    thecount = 0
    # Store the answer and the number of calculation variables in the session
    session['answer'] = theanswer
    session['count'] = thecount

    return render_template("index.html", answer=theanswer, count=thecount)


</t>
<t tx="amd.20151020232503.1"></t>
<t tx="amd.20151020232703.1">@app.route('/user/&lt;name&gt;')
def user(name):
    return render_template("user.html", name=name)</t>
<t tx="amd.20151020232845.1">@app.route('/req1')
def req1():
    user_agent = request.headers.get('User-Agent')
    return '&lt;p&gt;Your browser is %s&lt;/p&gt;' % user_agent</t>
<t tx="amd.20151020233400.1">@app.route('/red')
def red():
    # redirect to google
    return redirect("http://www.google.com")</t>
<t tx="amd.20151020234043.1"></t>
<t tx="amd.20151021000403.1">@app.route('/guessform')
def guessform():
    session["count"] += 1
    guess = session.get("guess")
    theanswer = session.get("answer")
    count = session.get("count")
    return render_template("guessform.html", guess=guess, answer=theanswer, count=count)</t>
<t tx="amd.20151021000629.1">@app.route('/docheck', methods=['POST'])
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
    if theanswer &lt; theguess:
        return render_template("toobig.html", guess=guess, answer=theanswer, count=count)
    elif theanswer &gt; theguess:
        return render_template("toosmall.html", guess=guess, answer=theanswer, count=count)
    else:
        # 
        # got the answer, get count from session
        thecount = session.get('count')
        return "Guess "+str(thecount)+" times, finally got the answer, the answer is "+str(theanswer)+": &lt;a href='/'&gt;Play again&lt;/a&gt;"
    return render_template("docheck.html", guess=guess)
 </t>
<t tx="leo.20200311103136.1">Location of openssl from https://www.msys2.org/

y:\msys64\mingw64\bin\openssl.exe

openssl req -x509 -nodes -days 600 -newkey rsa:2048 -keyout cd2020.key -out cd2020.crt</t>
<t tx="leo.20200311104223.1">https://github.com/coleifer/peewee</t>
<t tx="leo.20200311104947.1">https://github.com/mdecourse/wcms-scrum1

Pybean reference:

https://github.com/jonathan-kosgei/pybean

https://github.com/johndoe46/PyBean

from pybean import Store, SQLiteWriter
library = Store(SQLiteWriter(":memory:", frozen=False))
book = library.new("book")
book.title = "Boost development with pybean"
book.author = "Charles Xavier"
library.save(book)
for book in library.find("book","author like ?",["Charles Xavier"]):
        print book.title
library.delete(book)
library.commit()

To Create a new database table

pybean.setup()
book = pybean.dispense(bean_type)
pybean.db.commit()
pybean.close()

To store data in a database table

pybean.setup()
bean_type = 'book'
bookone.name = 'Eragon'
bookone.author = 'Christopher Paolini'
bean_id = pybean.store(bookone)
pybean.db.commit()

To load data from a database table

pybean.setup()
bean_type = 'book'
bookone = pybean.dispense(bean_type)
bookone.name = 'Eldest'
bookone.author = 'Christopher Paolini'
bean_id = pybean.store(bookone)
bean = pybean.load(bean_type, bean_id)
#print(bean)

To enter multiple rows in a database table

pybean.setup()
bean_type1 = 'movies'
bean_type2 = 'books'
beans = pybean.dispenseAll(bean_type1, bean_type2)
pybean.db.commit()

To load multiple rows from a database table

pybean.setup()
bean_type = 'book'
book = pybean.dispense(bean_type)
book.title = 'The Inheritance'
id1 = pybean.store(book)
page = pybean.dispense(bean_type)
page.number = 145
id2 = pybean.store(page)
#print(id2, page)
beans = pybean.loadAll(bean_type, id1, id2)
#print(beans)
pybean.close()

To delete a row in a database table

pybean.setup()
bean_type = 'book'
bookone = pybean.dispense(bean_type)
bookone.name = 'Eldest'
bookone.author = 'Christopher Paolini'
id = pybean.store(bookone)
pybean.trash(bookone.type, id)
pybean.close()

To delete multiple rows in a database table

pybean.setup()
bean_type1 = 'book'
bean_type2 = 'book'
beans = pybean.dispenseAll(bean_type1, bean_type2)
beans[0].name = 'The Man from St.Petersburg'
beans[1].name = 'Preface'
id1 = pybean.store(beans[0])
id2 = pybean.store(beans[1])
pybean.trashAll('book', id1, id2)
pybean.close()

To delete a database table

pybean.setup()
cursor = pybean.db.cursor()
bean_type = 'book'
book = pybean.dispense(bean_type)
book.title = 'Head Fist C#'
id = pybean.store(book)
pybean.wipe('book')
pybean.close()

To delete an entire database

pybean.setup()
pybean.nuke()</t>
<t tx="leo.20200409150450.1">@language python
import random
import requests

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
print("Expected number of member list:" + str(numList))

output = ""
gth = 1
inc = 0

# use shuffle method of random module to shuffle studList
random.shuffle(studList)
output += "Before sort: \n"
for i in numList:
    # print 20 * sign
    output += '=' * 20 + "\n";
    output += "group " + str(gth) + " 有 " + str(i) + " 人: \n"
    # reset group list
    gpList = []
    for j in range(i):
        output += studList[j+inc] + "\n"
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
output += '=' * 25 + "\n"
output += 'Sorted result:\n'
gth = 1
 
# list sorted data seperated by \n
for i in range(len(group)):
    # print seperated mark
    output += '=' * 20 + "\n"
    output += "group" + str(gth) + "\n"
    gpList = []

    for j in range(len(group[i])):
        output += str(group[i][j]) + "\n"

    gth = gth + 1

print(output)</t>
<t tx="leo.20200409151441.1">@app.route("/randomgrouping")
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
    output += "Before sort: &lt;br /&gt;"
    for i in numList:
        # print 20 * sign
        output += '=' * 20 + "&lt;br /&gt;";
        output += "group " + str(gth) + " has " + str(i) + " members:&lt;br /&gt;"
        # reset group list
        gpList = []
        for j in range(i):
            output += studList[j+inc] + "&lt;br /&gt;"
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
    output += '=' * 20 + "&lt;br /&gt;"
    output += 'Sorted result:&lt;br /&gt;'
    gth = 1

    # list sorted data seperated by \n
    for i in range(len(group)):
        # print seperated mark
        output += '=' * 20 + "&lt;br /&gt;"
        output += "group" + str(gth) + "&lt;br /&gt;"
        gpList = []

        for j in range(len(group[i])):
            output += str(group[i][j]) + "&lt;br /&gt;"

        gth = gth + 1

    print(output)
    return output</t>
<t tx="leo.20200409151603.1"># get the distributed list among each group
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
    return splits;</t>
</tnodes>
</leo_file>
