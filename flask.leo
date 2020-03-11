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
<v t="amd.20150313083555.45"><vh>有關本專案</vh></v>
<v t="leo.20200311103136.1"><vh>generate self-signed certificate</vh></v>
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
<t tx="amd.20150313083555.45">Python 與  Flask 在協同產品機械設計上的應用

2020.03.11 啟動
</t>
<t tx="amd.20151020232112.1"># setup static directory
@app.route('/static/&lt;path:path&gt;')
def send_static(path):
    return send_from_directory('static', path)</t>
<t tx="amd.20151020232140.1">@app.route("/")
def index():
    #這是猜數字遊戲的起始表單, 主要在產生答案, 並且將 count 歸零
    # 將標準答案存入 answer session 對應區
    theanswer = random.randint(1, 100)
    thecount = 0
    # 將答案與計算次數變數存進 session 對應變數
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
    # 重新導向 google
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
    # session[] 存資料
    # session.get() 取 session 資料
    # 利用 request.form[] 取得表單欄位資料, 然後送到 template
    guess = request.form["guess"]
    session["guess"] = guess
    # 假如使用者直接執行 doCheck, 則設法轉回根方法
    if guess is None:
        redirect("/")
    # 從 session 取出 answer 對應資料, 且處理直接執行 docheck 時無法取 session 值情況
    try:
        theanswer = int(session.get('answer'))
    except:
        redirect("/")
    # 經由表單所取得的 guess 資料型別為 string
    try:
        theguess = int(guess)
    except:
        return redirect("/guessform")
    # 每執行 doCheck 一次,次數增量一次
    session["count"] += 1
    count = session.get("count")
    # 答案與所猜數字進行比對
    if theanswer &lt; theguess:
        return render_template("toobig.html", guess=guess, answer=theanswer, count=count)
    elif theanswer &gt; theguess:
        return render_template("toosmall.html", guess=guess, answer=theanswer, count=count)
    else:
        # 已經猜對, 從 session 取出累計猜測次數
        thecount = session.get('count')
        return "猜了 "+str(thecount)+" 次, 終於猜對了, 正確答案為 "+str(theanswer)+": &lt;a href='/'&gt;再猜&lt;/a&gt;"
    return render_template("docheck.html", guess=guess)
 </t>
<t tx="leo.20200311103136.1">Location of openssl from https://www.msys2.org/

y:\msys64\mingw64\bin\openssl.exe

openssl req -x509 -nodes -days 600 -newkey rsa:2048 -keyout cd2020.key -out cd2020.crt</t>
</tnodes>
</leo_file>
