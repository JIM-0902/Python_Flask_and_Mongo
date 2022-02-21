# 更新文件

"""

* 更新一筆文件 :更新符合條件的一筆文件欄位
* 集合.update_one(篩選條件,更新的資訊)

* 更新多筆文件
* 集合.update_many(篩選條件,更新的資訊)

* 覆蓋/新增欄位:使用$set覆蓋/新增欄位
* 加減數字欄位:使用$inc加減數字欄位
* 乘除數字欄位:使用$mul乘除數字欄位
* 清除欄位    :使用$unset清除欄位

* 符合篩選條件的文件數量
  result.matched_count
* 實際完成更新的文件數量
  result.modified_count
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

# 更新集合中的一筆文件資料
result=collection.update_one(
    {
        "name":"jimmy"
    }, 
    {"$set":
      {
        "gender":"女"
      }
    })
    
print("符合篩選條件的文件數量",result.modified_count)
print("實際更新的文件數量",result.matched_count)