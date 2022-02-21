# 超連結: <a href='網址'>可點擊的內容</a>
# 圖片 <img src='圖片網址'/>

from flask import Flask
from flask import request
# 載入 render_template 套件
from flask import render_template

app =Flask(__name__,static_folder="static",static_url_path="/")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page")
def page():
    return render_template("page.html")

app.run(port=4000)