# 要求字串處理 Query String

# 通訊協定://主機名稱:阜號/路徑?要求字串( Query String)

"""
格式說明 : 參數名稱=資料

程式語法
request.args.get("參數名稱",預設值)

"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__,static_folder='public',static_url_path="/")

# 建立路徑 /getSum 對應的處理函式
# 利用要求字串 (Query Sttring) 提供彈性 /getSum?min=最小數字&max=最大數字

@app.route("/getSum")
def getSum(): # min+...+max
    # 接收要求字串中的參數
    maxNumber=request.args.get("max",100)
    maxNumber = int(maxNumber)
    minNumber=request.args.get("min",100)
    minNumber = int(minNumber)
    result=0
    for n in range(minNumber,maxNumber):
        result+=n
    # 把結果回應給前端
    return "結果:"+str(result)

@app.route("/")
def index():

    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else :
        return "您好，歡迎光臨"

# 啟動網站伺服器，可透過 port 參數指定阜號
app.run(port=3000)

