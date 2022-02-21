"""
1.取得集合中的第一筆文件資料
* 集合.find_one()

2.根據編號取得文件資料
* 文件編號是一個objectld物件，必須先從bson.objectid封包載入
* 集合.find_one(文件編號)

3. 取得文件資料中的欄位
* 文件資料["欄位名稱"]

4. 取得所有文件資料
* 集合.find()
"""

# 載入 pymongo 套件
import pymongo
from bson.objectid import ObjectId

# 連線到MongoDB雲端資料庫
client = pymongo.MongoClient("mongodb+srv://Jimmy:oiet123456@mycluter.shpuj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# 把資料放進資料庫中
# 選擇操作test資料庫(沒有的話會自動建一個(test))
db = client.mywebsite

# 選擇操作users集合
collection = db.users

# 取得集合中第一筆資料
# data = collection.find_one()
# print(data)

# 根據 ObjectID 取得文件資料
# data = collection.find_one(
#     ObjectId("620f33719b5fb7ede00ed422")
# )
# print(data)

# 取得文件資料中的欄位
# print(data["_id"])

# 一次取得多筆文件資料
cursor = collection.find()
print(cursor)

for doc in cursor:
    print(doc)

# 把資料新增到集合中
# collection.insert_one({
#     "name":"tim",
#     "gender":"girl",
#     "level":1
# })

# print("資料新增成功")


