# 載入Flask
from flask import Flask

# 建立application物件
app = Flask(__name__)

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