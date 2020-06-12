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
# calculate pagenating
import math

# for login_required decorator
from functools import wraps

# for sqlite3 資料庫
import sqlite3
from contextlib import closing

# for add_entry
import datetime

# for GDrive upload
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# for get mimeType of uploaded file
import mimetypes

# for uploadToGDrive3
# pip install google-api-python-client
# https://github.com/googleapis/google-api-python-client
import pickle
from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload

# for filegdupload
import pickle
import codecs
import json

# for mako template engine
# for mako template 系統
from mako.template import Template
from mako.lookup import TemplateLookup

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T', report_errors=False)

# 確定程式檔案所在目錄, 在 Windows 有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
download_dir = _curdir + "/downloads/"
template_root_dir = _curdir + "/templates"
    
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
        # need to check if this work with Windows
        conn = sqlite3.connect(_curdir+"/db/database.db")
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
    print("do nothing")
@app.before_request
def before_request():
    # need to check if this works with Windows
    g.db = sqlite3.connect(_curdir+"/db/database.db")
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
    template_lookup = TemplateLookup(directories=[template_root_dir])
    rocTemplate = template_lookup.get_template("drawROC.html")
    return rocTemplate.render()
    
@app.route("/menu")
@login_required
def menu():
    menuList = ["guess", "drawROC", "randomgrouping", "show_entries", "fileuploadform", "download_list"]
    template_lookup = TemplateLookup(directories=[template_root_dir])
    menuTemplate = template_lookup.get_template("menu.html")
    return menuTemplate.render(menuList=menuList)
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

    template_lookup = TemplateLookup(directories=[template_root_dir])
    guessTemplate = template_lookup.get_template("guess.html")
    return guessTemplate.render(answer=theanswer, count=thecount, user=user)


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
    
    template_lookup = TemplateLookup(directories=[template_root_dir])
    guessTemplate = template_lookup.get_template("guessform.html")
    return guessTemplate.render(guess=guess, answer=theanswer, count=count)
@app.route('/docheck', methods=['POST'])
@login_required
def docheck():
    template_lookup = TemplateLookup(directories=[template_root_dir])
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
    tooBigTemplate = template_lookup.get_template("toobig.html")
    tooSmallTemplate = template_lookup.get_template("toosmall.html")
    if theanswer < theguess:
        return tooBigTemplate.render(guess=guess, answer=theanswer, count=count)
    elif theanswer > theguess:
        return tooSmallTemplate.render(guess=guess, answer=theanswer, count=count)
    else:
        # 
        # got the answer, get count from session
        thecount = session.get('count')
        return "Guess "+str(thecount)+" times, finally got the answer, the answer is "+str(theanswer)+": <a href='/guess'>Play again</a>"

    doCheckTemplate = template_lookup.get_template("docheck.html")
    return doCheckTemplate.render(guess=guess)
 
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

    #print(output)
    
    # add grouping result into grouping table of /db/database.db
    date = datetime.datetime.now().strftime("%b %d, %Y - %H:%M:%S")
    user = session.get("user")
    result = str(group)
    # 希望新增重複資料查驗功能
    g.db.execute('insert into grouping (user , date, result, memo) values (? , ?, ?, ?)',
            (user, date, result, "memo"))
    g.db.commit()
    flash('已經新增一筆資料!')
    return output
@app.route('/add_entry',methods=['POST'])
@login_required
def add_entry():
    date = datetime.datetime.now()
    # 希望新增重複資料查驗功能
    g.db.execute('insert into grouping (user , date, result, memo) values (? , ?, ?, ?)',
            (request.form['user'], date, request.form['result'], \
            request.form['memo']))
    g.db.commit()
    flash('已經新增一筆資料!')
    return redirect(url_for('show_entries'))
# set default value of the variables accordingly
@app.route('/show_entries', defaults={'page': 1, 'item_per_page': 10})
@app.route('/show_entries/<int:page>', defaults={'item_per_page': 10})
@app.route('/show_entries/<int:page>/<int:item_per_page>')
@login_required
# 內定每頁顯示 10 筆資料, 從第1頁開始
def show_entries(page, item_per_page):
    # 先取得資料總筆數
    cur = g.db.execute('select * from grouping;')
    total_number = len(cur.fetchall())
    query_string = 'select id, user , date, result, memo from grouping order by id desc limit '+str(item_per_page)+' offset '+str((page-1)*item_per_page)
    cur = g.db.execute(query_string)
    grouping = [dict(id=row[0], user=row[1], date=row[2], result=row[3], memo=row[4]) for row in cur.fetchall()]
    totalpage = math.ceil(total_number/int(item_per_page))
    login = session.get('login')
    template_lookup = TemplateLookup(directories=[template_root_dir])
    showEntriesTemplate = template_lookup.get_template("show_entries.html")
    return showEntriesTemplate.render(login=login, grouping = grouping, \
                        total_number=total_number, page=page, \
                        item_per_page=item_per_page, totalpage=totalpage)             
    
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
# root of the system can not set "login_required" decorator
# 開始改用 Make 作為 Template
def index():
    template_lookup = TemplateLookup(directories=[template_root_dir])
    indexTemplate = template_lookup.get_template("index.html")
    return indexTemplate.render()
@app.route('/alogin' , methods=['GET' , 'POST'])
def alogin():
    error = None
    if request.method == 'POST':
        if request.form['username'] != "admin":
            error = '錯誤!'
        elif request.form['password'] != "admin":
            error = '錯誤!'
        else :
            session['login'] = True
            session['user'] = "alogin"
            flash('已經登入!')
            return redirect(url_for('menu'))
    #return render_template('alogin.html' , error = error)
    template_lookup = TemplateLookup(directories=[template_root_dir])
    aloginTemplate = template_lookup.get_template("alogin.html")
    return aloginTemplate.render()
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
        template_lookup = TemplateLookup(directories=[template_root_dir])
        loginTemplate = template_lookup.get_template("login.html")
        CALLBACK_URL = "https://localhost:8443/menu"
        
        return loginTemplate.render(result=result, CALLBACK_URL=CALLBACK_URL)

    # Don't forget to return the response.
    return response
@app.route('/logout')
def logout():
    session.pop('login' , None)
    session.pop('user', None)
    flash('Logged out!')
    return redirect(url_for('index'))
@login_required
@app.route('/fileaxupload', methods=['POST'])
# ajax jquery chunked file upload for flask
def fileaxupload():
    # need to consider if the uploaded filename already existed.
    # right now all existed files will be replaced with the new files
    filename = request.args.get("ax-file-name")
    flag = request.args.get("start")
    if flag == "0":
        file = open(_curdir + "/downloads/" + filename, "wb")
    else:
        file = open(_curdir + "/downloads/" + filename, "ab")
    file.write(request.stream.read())
    file.close()
    return "files uploaded!"


# 希望直接由 browser client 將檔案以 chunked 大小送往 GD 儲存
@login_required
@app.route('/filegdupload', methods=['POST'])
# ajax jquery chunked file upload for flask
def filegdupload():
    
    with open('./../gdrive_write_token.pickle', 'rb') as token:
        gdrive = pickle.load(token, encoding='utf-8')

    with open("./../gdrive_uploaded_id.txt", 'r') as content_file:
        folderID = content_file.read()

    #print(gdrive.token)
    ACCESS_TOKEN = gdrive.token
    # need to consider if the uploaded filename already existed.
    # right now all existed files will be replaced with the new files
    fileName = request.args.get("ax-file-name")
    
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}
    mimeType = mimetypes.MimeTypes().guess_type(fileName)[0]
    metadata = {
        'name': fileName,
        'mimeType': mimeType,
        # 注意: 必須提供數列格式資料
        'parents': [folderID]
        }

    files = {
    "data": ("metadata", json.dumps(metadata), "application/json; charset=UTF-8"),
    "file": request.stream.read()
    }

    response = requests.post("https://www.googleapis.com/upload/drive/v2/files", headers=headers, files=files)

    #return response 
    '''
    flag = request.args.get("start")
    if flag == "0":
        file = open(_curdir + "/downloads/" + filename, "wb")
    else:
        file = open(_curdir + "/downloads/" + filename, "ab")
    file.write(request.stream.read())
    file.close()
    '''
    return "files uploaded!"
    
@login_required
@app.route('/fileuploadform', defaults={'edit':1})
@app.route('/fileuploadform/<path:edit>')
def fileuploadform(edit):
    '''
    準備改寫為 template 傳回上傳表單, 或加上其他相關欄位
    '''
    template_lookup = TemplateLookup(directories=[template_root_dir])
    uploadFormTemplate = template_lookup.get_template("uploadform.html")
    return uploadFormTemplate.render()



@app.route('/download/', methods=['GET'])
def download():

    """Download file using URL
    """

    filename = request.args.get('filename')
    type = request.args.get('type')
    if type == "files":
        return send_from_directory(download_dir, filename=filename)
    else:
    # for image files
        return send_from_directory(image_dir, filename=filename)
    

@app.route('/downloads/<path:path>')
def downloads(path):

    """Send files in downloads directory
    """

    return send_from_directory(_curdir+"/downloads/", path)

@app.route('/download_list', methods=['GET'])
@login_required
def download_list():
    '''
    準備改寫為 template based
    '''

    """List files in downloads directory
    """

    if not request.args.get('edit'):
        edit= 1
    else:
        edit = request.args.get('edit')
    if not request.args.get('page'):
        page = 1
    else:
        page = request.args.get('page')
    if not request.args.get('item_per_page'):
        item_per_page = 10
    else:
        item_per_page = request.args.get('item_per_page')
    if not request.args.get('keyword'):
        keyword = ""
    else:
        keyword = request.args.get('keyword')
        session['download_keyword'] = keyword

    files = os.listdir(download_dir)
    if keyword != "":
        files = [elem for elem in files if str(keyword) in elem]
    files.sort()
    total_rows = len(files)
    totalpage = math.ceil(total_rows/int(item_per_page))
    starti = int(item_per_page) * (int(page) - 1) + 1
    endi = starti + int(item_per_page) - 1
    outstring = "<form method='post' action='delete_file'>"
    notlast = False
    if total_rows > 0:
        outstring += "<br />"
        if (int(page) * int(item_per_page)) < total_rows:
            notlast = True
        if int(page) > 1:
            outstring += "<a href='"
            outstring += "download_list?&amp;page=1&amp;item_per_page=" + str(item_per_page) + \
                                "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'><<</a> "
            page_num = int(page) - 1
            outstring += "<a href='"
            outstring += "download_list?&amp;page=" + str(page_num) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Previous</a> "

        span = 10

        for index in range(int(page)-span, int(page)+span):
            if index>= 0 and index< totalpage:
                page_now = index + 1 
                if page_now == int(page):
                    outstring += "<font size='+1' color='red'>" + str(page) + " </font>"
                else:
                    outstring += "<a href='"
                    outstring += "download_list?&amp;page=" + str(page_now) + "&amp;item_per_page=" + \
                                        str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
                    outstring += "'>"+str(page_now) + "</a> "

        if notlast == True:
            nextpage = int(page) + 1
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(nextpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Next</a>"
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(totalpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>>></a><br /><br />"

        if (int(page) * int(item_per_page)) < total_rows:
            notlast = True
            outstring += downloadlist_access_list(files, starti, endi) + "<br />"
        else:
            outstring += "<br /><br />"
            outstring += downloadlist_access_list(files, starti, total_rows) + "<br />"

        if int(page) > 1:
            outstring += "<a href='"
            outstring += "download_list?&amp;page=1&amp;item_per_page=" + str(item_per_page) + \
                                "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'><<</a> "
            page_num = int(page) - 1
            outstring += "<a href='"
            outstring += "download_list?&amp;page=" + str(page_num) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Previous</a> "

        span = 10

        for index in range(int(page)-span, int(page)+span):
        #for ($j=$page-$range;$j<$page+$range;$j++)
            if index >=0 and index < totalpage:
                page_now = index + 1
                if page_now == int(page):
                    outstring += "<font size='+1' color='red'>" + str(page)+" </font>"
                else:
                    outstring += "<a href='"
                    outstring += "download_list?&amp;page=" + str(page_now) + \
                                        "&amp;item_per_page=" + str(item_per_page) + \
                                        "&amp;keyword=" + str(session.get('download_keyword'))
                    outstring += "'>" + str(page_now)+"</a> "

        if notlast == True:
            nextpage = int(page) + 1
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(nextpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>Next</a>"
            outstring += " <a href='"
            outstring += "download_list?&amp;page=" + str(totalpage) + "&amp;item_per_page=" + \
                                str(item_per_page) + "&amp;keyword=" + str(session.get('download_keyword'))
            outstring += "'>>></a>"
    else:
        outstring += "no data!"
    outstring += "<br /><br /><input type='submit' value='delete'><input type='reset' value='reset'></form>"


    return "<h1>Download List</h1>" + outstring + "<br/><br /></body></html>"


def downloadlist_access_list(files, starti, endi):
    
    """List files function for download_list
    """
    
    # different extension files, associated links were provided
    # popup window to view images, video or STL files, other files can be downloaded directly
    # files are all the data to list, from starti to endi
    # add file size
    outstring = ""
    for index in range(int(starti)-1, int(endi)):
        fileName, fileExtension = os.path.splitext(files[index])
        fileExtension = fileExtension.lower()
        fileSize = sizeof_fmt(os.path.getsize(download_dir+"/"+files[index]))
        # images files
        if fileExtension == ".png" or fileExtension == ".jpg" or fileExtension == ".gif":
            outstring += '<input type="checkbox" name="filename" value="' + \
                              files[index] + '"><a href="javascript:;" onClick="window.open(\'/images/' +  \
                              files[index] + '\',\'images\', \'catalogmode\',\'scrollbars\')">' + \
                              files[index] + '</a> (' + str(fileSize) + ')<br />'
        # stl files
        elif fileExtension == ".stl":
            outstring += '<input type="checkbox" name="filename" value="' + \
                              files[index] + '"><a href="javascript:;" onClick="window.open(\'/static/viewstl.html?src=' + '/downloads/' + \
                              files[index] + '\',\'images\', \'catalogmode\',\'scrollbars\')">' + \
                              files[index] + '</a> (' + str(fileSize) + ')<br />'
        # flv files
        elif fileExtension == ".flv":
            outstring += '<input type="checkbox" name="filename" value="' + \
                              files[index] + '"><a href="javascript:;" onClick="window.open(\'/flvplayer?filepath=/downloads/' + \
            files[index] + '\',\'images\', \'catalogmode\',\'scrollbars\')">' + files[index] + '</a> (' + str(fileSize) + ')<br />'
        # direct download files
        else:
            outstring += "<input type='checkbox' name='filename' value='" + files[index] + \
                              "'><a href='./../downloads/" + files[index] + "'>" + files[index] + \
                              "</a> (" + str(fileSize) + ")<br />"
    return outstring


# downloads 方法主要將位於 downloads 目錄下的檔案送回瀏覽器
def sizeof_fmt(num):
    """size formate"""
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')
@app.route('/delete_file', methods=['POST'])
@login_required
def delete_file():

    """Delete user uploaded files
    """
    # use request.form.getlist() allow multiple select
    filename = request.form.getlist('filename')

    if filename is None:
        outstring = "no file selected!"
        return "<h1>Delete Error</h1>" + \
                   outstring + "<br/><br /></body></html>"
    outstring = "delete all these files?<br /><br />"
    outstring += "<form method='post' action='doDelete'>"
    # only one file is selected
    if isinstance(filename, str):
        outstring += filename + "<input type='hidden' name='filename' value='" + \
                            filename + "'><br />"
    else:
        # multiple files selected
        for index in range(len(filename)):
            outstring += filename[index] + "<input type='hidden' name='filename' value='" + \
                                filename[index]+"'><br />"
    outstring += "<br /><input type='submit' value='delete'></form>"

    return "<h1>Download List</h1>" + \
               outstring + "<br/><br /></body></html>"


@app.route('/doDelete', methods=['POST'])
@login_required
def doDelete():

    """Action to delete user uploaded files
    """

    # delete files
    # allow multiple files selection
    filename = request.form.getlist('filename')
    outstring = "all these files will be deleted:<br /><br />"
    # only select one file
    if isinstance(filename, str):
        try:
            os.remove(download_dir + "/" + filename)
            outstring += filename + " deleted!"
        except:
            outstring += filename + "Error, can not delete files!<br />"
    else:
        # multiple files selected
        for index in range(len(filename)):
            try:
                os.remove(download_dir + "/" + filename[index])
                outstring += filename[index] + " deleted!<br />"
            except:
                outstring += filename[index] + "Error, can not delete files!<br />"


    return "<h1>Download List</h1>" + \
               outstring + "<br/><br /></body></html>"


@app.route('/saveToDB' , methods=['POST'])
@login_required
def saveToDB():

    """axuploader.js 將檔案上傳後, 將上傳檔案名稱數列, 以 post 回傳到 Flask server.
    
    截至這裡, 表示檔案已經從 client 上傳至 server, 可以再設法通過認證, 將 server 上的檔案上傳到對應的 Google Drive, 並且在上傳後的 GDrive 目錄, 設定特定擷取權限 (例如: 只允許 @gm 用戶下載.
    以下則可將 server 上傳後的擷取目錄與 GDrive 各檔案 ID 存入資料庫, 而檔案擷取則分為 server 擷取與 GDrive 擷取等兩種 url 連結設定
    """

    if request.method == "POST":
        files = request.form["files"]
        # split files string
        files = files.split(",")
        # files 為上傳檔案名稱所組成的數列
        for i in range(len(files)):
            # 逐一將已經存在 server downloads 目錄的檔案, 上傳到 GDrive uploaded 目錄
            fileName = files[i]
            fileLocation = _curdir + "/downloads/" + fileName
            mimeType = mimetypes.MimeTypes().guess_type(fileLocation)[0]
            # for GDrive v2
            #gdriveID = uploadToGdrive(fileName, mimeType)
            # for GDrive v3
            gdriveID = uploadToGdrive3(fileName, mimeType)
            fileSize = str(round(os.path.getsize(fileLocation)/(1024*1024.0), 2)) + " MB"
            date = datetime.datetime.now().strftime("%b %d, %Y - %H:%M:%S")
            user = session.get("user")
            print(user + "|" + str(fileSize) + "|" + str(mimeType) + "|"  + gdriveID)
            # 逐一將上傳檔案名稱存入資料庫, 同時存入mimeType, fileSize 與 gdriveID
            # 資料庫欄位
            #g.db.execute('insert into grouping (user , date, fileName, mimeType, fileSize, memo) values (?, ?, ?, ?, ?, ?)',(user, date, fileName, mimeType, fileSize, "memo"))
            #g.db.commit()
            #flash('已經新增一筆 upload 資料!')
    return "Uploaded fileName and gdriveID save to database"
def uploadToGdrive(fileName, mimeType):
    gauth = GoogleAuth()
    # 必須使用 desktop 版本的 client_secrets.json
    gauth.LoadClientConfigFile("./../gdrive_desktop_client_secrets.json")
    drive = GoogleDrive(gauth)
    
    '''
    # View all folders and file in your Google Drive
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
      print('Title: %s, ID: %s' % (file['title'], file['id']))
      # Get the folder ID that you want
      # 檔案會上傳到根目錄下的 uploaded  目錄中
      if(file['title'] == "uploaded"):
          fileID = file['id']
    '''
    # GDrive 上 uploaded 目錄的 fileID
    with open("./../gdrive_uploaded_id.txt", 'r') as content_file:
        fileID = content_file.read()
    
    # 由上述目錄外的檔案讀取 uploaded 目錄對應 ID
    #fileID = "your_folder_file_ID"
    # 上傳檔案名稱為輸入變數
    #fileName = "DemoFile.pdf"
    filePath = _curdir + "/downloads/"
    # parents 為所在 folder, 亦即 uploaded 目錄, fileID 為 uploaded 目錄的 ID
    file1 = drive.CreateFile({"mimeType": mimeType, "parents": [{"kind": "drive#fileLink", "id": fileID}], "title":  fileName})
    file1.SetContentFile(filePath + fileName)
    file1.Upload() # Upload the file.
    # 傳回與上傳檔案對應的 GDrive ID, 將會存入資料庫 gdiveID 欄位
    return file1['id']
    #print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))   
    #print("upload fileID:" + str(file1['id']))
    # 以下為下載檔案測試
    # file2 = drive.CreateFile({'id': file1['id']})
    #file2.GetContentFile('./test/downloaded_ModernC.pdf') # Download file as 'downloaded_ModernC.pdf under directory test'.
    
    '''
    file1.Trash()  # Move file to trash.
    file1.UnTrash()  # Move file out of trash.
    file1.Delete()  # Permanently delete the file.
    '''
def uploadToGdrive3(fileName, mimeType):
    # get upload folder id
    # GDrive 上 uploaded 目錄的 fileID
    with open("./../gdrive_uploaded_id.txt", 'r') as content_file:
        folderID = content_file.read()

    creds = None
    with open('./../gdrive_write_token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # 讀進既有的 token, 建立 service
    driveService = build('drive', 'v3', credentials=creds)

    metadata = {
        'name': fileName,
        'mimeType': mimeType,
        # 注意: 必須提供數列格式資料
        'parents': [folderID]
        }

    filePath = _curdir + "/downloads/" + fileName
    media = MediaFileUpload(filePath,
                                            mimetype=mimeType,
                                            chunksize=1024*1024,
                                            resumable=True
                                            )

    gdFile = driveService.files().create(
        body=metadata,
        media_body=media,
        fields='id'
    ).execute()
    fileID = gdFile.get("id")

    return fileID

if __name__ == "__main__":
    app.run()

