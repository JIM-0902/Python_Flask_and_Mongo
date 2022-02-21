# 樣本引擎:網站後端回應給前端的方式
"""
1. 直接回應字串
2. 回應JSON格式字串
3. 重新導向
4. 使用樣板引擎

使用樣板引擎:根據樣板檔案，產生字串，傳送到前端

1.方便撰寫複雜的前端程式
2.方便在回應中，動態的帶入資料

樣板檔案必須建立在專案的Templates子資料夾底下

# 使用樣板檔案 : 取得樣板檔案中的文字，傳送到前端

1. 透過render_template()根據樣板檔案的內容產生文字串
   
   @app.route("/")
   def index():
       return render_template(檔案路徑)

建立樣本檔案，定義資料欄位:在樣板檔案中定義動態處理的欄位

* 利用{{資料欄位的名稱}}定義欄位
* 例如，在樣板檔案中加入以下的欄位
   您好，{{name}}，歡迎光臨


"""

from flask import Flask
from flask import request
# 載入 render_template 套件
from flask import render_template

app =Flask(__name__,static_folder="static",static_url_path="/")
@app.route("/")
def index():
    return render_template("index",name='小明')

app.run(port=4000)

