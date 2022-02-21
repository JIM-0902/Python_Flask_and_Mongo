# 請求(HTTP Request):前端透過網址連線到後端的正式稱呼

"""
Flack接收請求的流程
1. 前端發送請求
2. Flask套件協助我們處理網路連線底層:負責接收請求，並將相關資訊封裝在request物件中
3. 根據路由，決定要怎麼處理請求

Request 物件:透過這個物件，取得請求相關資訊
使用方式:
1. 載入reuqest物件
2. 在路由對應的函式中直接使用request取得物件
3. 進一步取得相關資訊

使用request物件的各種屬性
1. method 請求方法
2. scheme 通訊協定
3. host   主機名稱
4. path   路徑
5. url    完整網址

Request Headers :取得當前請求的標頭(附加資訊)
使用request物件的headers屬性。常見標頭如下
1. user-agent
2. accept-language
3. referrer
"""
# 載入Flask
from flask import Flask
# 載入request物件
from flask import request

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
    #print("請求方法",request.method)
    #print("通訊協定",request.scheme)
    #print("路徑", request.path)
    #print("完整的路徑", request.url)
    #print("瀏覽器和作業系統", request.headers.get("user-agent"))
    #print("語言偏好", request.headers.get("accept-language"))
    #print("引薦網址", request.headers.get("referrer"))
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else :
        return "您好，歡迎光臨"

# 啟動網站伺服器，可透過 port 參數指定阜號
app.run(port=3000)