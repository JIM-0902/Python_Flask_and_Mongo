"""
比喻
網址:收件地址
方法:普通信件，限時快遞

最常見的方法:GET，POST

# 使用GET方法做前後端互動

* 前端HTML程式
<form action="網址路徑" method="GET">
   <input type = 'text' name='data'/>
   <button>點擊送出表單</button>
</form>

* 後端python程式
@app.route('網址路徑',methods=["GET"])
def handle():
    input=request.args.get("data","")
    return "給前端的回應"


# 使用HOST方法做前後端互動

* 前端HTML程式
<form action="網址路徑" method="HOST">
   <input type = 'text' name='data'/>
   <button>點擊送出表單</button>
</form>

* 後端python程式
@app.route('網址路徑',methods=["HOST"])
def handle():
    input=request.form["data"]
    return "給前端的回應"

* 使用者狀態管理
First app route

name = request.args.get("name",None)
session["data"]=name
return "您好"+name

Second app route
name = session["data"]
return name+".很高興見到你"

"""