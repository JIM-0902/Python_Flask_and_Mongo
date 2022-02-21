# html表單
"""
前端HTML程式
<form action="網址路徑">
   <input type="text" name="data"/>
   <button>點擊送出表單</button>
</form>

後端python程式
@app.route("網址路徑")
def handle():
    input = request.args.get("data","") 
    return "給前端的回應"

"""

# 超連結: <a href='網址'>可點擊的內容</a>
# 圖片 <img src='圖片網址'/>

from flask import Flask
from flask import request
# 載入 render_template 套件
from flask import render_template

app =Flask(__name__,static_folder="static",static_url_path="/")

# 處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("index.html")

# 處理路徑 /page 的對應函式
@app.route("/page")
def page():
    return render_template("page.html")

@app.route("/show")
def show():
    name=request.args.get("n",None)
    return "歡迎光臨"+name

# 處理路徑 /calculate 的對應函式
@app.route("/cal")
def cal():
    maxnumber=request.args.get("cal"," ")
    maxnumber=int(maxnumber)
    result=0
    for n in range(1,maxnumber+1):
        result+=n
    # 結合Query_String變成動態變數
    # data=str(result)
    return render_template("result.html",data=str(result))

app.run(port=4000)