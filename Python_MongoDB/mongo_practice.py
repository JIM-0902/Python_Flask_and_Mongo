# 載入 pymongo 套件
import pymongo

# 連線到MongoDB雲端資料庫
client = pymongo.MongoClient("mongodb+srv://Jimmy:oiet123456@mycluter.shpuj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# 把資料放進資料庫中
# 選擇操作test資料庫(沒有的話會自動建一個(test))
db = client.test

# 選擇操作users集合
collection = db.users

# 把資料新增到集合中
collection.insert_one({
    "name":"澎澎",
    "gender":"男"
})

print("資料新增成功")
