"""
1. 直接回應字串:將字串透過網路，傳送到前端
   return 字串

2. 回應JSON格式字串:透過json.dumps()將字典型態的資料轉換成JSON格式字串
   return json.dumps(字典)

3. 重新導向:將使用者導向到另一個網址路徑
   透過 redirect()將使用者導向到特定網址路徑
   return redirect(網址路徑)
"""

# 載入Flask
from flask import Flask
# 載入request物件
from flask import request
# 載入redirect函式
from flask import redirect
import json

# 建立application物件，可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/www'
)
# 所有在static資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱

# 建立路徑 /en/ 對應的處理函式
@app.route("/en/")
def index_english():
    return json.dumps({
            "status":"ok",
            "text":"Hello World"
        })
    

@app.route("/zw/")
def index_chinese():
    return json.dumps({
            "status":"ok",
            "text":"您好，歡迎光臨"
        }, ensure_ascii=False)


# 建立路徑 / 對應的處理函式
@app.route("/")
def index():
    # return redirect("/en/")
    # 導向到網址 https://www.google.com/
    # return redirect("https://www.google.com/") 
    
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else :
        return redirect("/zw/")
        # 指示不要用ASCII編碼處理中文
    

# 啟動網站伺服器，可透過 port 參數指定阜號
app.run(port=3000)