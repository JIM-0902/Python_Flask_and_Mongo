# 靜態檔案 : 不執行程式，直接將檔案送到前端
# 圖片檔案
# 影片檔案
# HTML,CSS,JavaScript
# 直接將檔案名稱對應到網址路徑

"""
程式不需要做任何更動

預設
操作方式
1. 建立static資料夾
2. 將檔案放入static資料夾中
3. 啟動伺服器
4. 前端使用/static/檔案名稱連線，取得檔案

自定(在建立Application物件時透過參數指定)
Flask(
    __name__,
    static_folder='資料夾名稱',
    static_url_path='對應的網址路徑'
)

"""

# 載入Flask
from flask import Flask

# 建立application物件，可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/www'
)
# 所有在static資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱

# 建立路徑 / 對應的處理函式
@app.route("/")
def index():
    return "Hello Flask"

# 建立路徑 /data 對應的處理函式
@app.route("/data")
def handleData():
    return "My Data"

# 動態路由:建立路徑 /user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def handleUser(username):
    return "Hello"+username

# 啟動網站伺服器，可透過 port 參數指定阜號
app.run(port=3000)