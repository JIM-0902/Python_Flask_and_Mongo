"""
複合的篩選條件
1. 條件必須同時成立 :使用$and結合多個條件

collection =db.website
data = collection.find_one(
    {
        "$and":[
            {"email":"test@test.com"},
            {"password":"test"}
        ]
    }
) 

2. 滿足任何一個條件就好 :使用$or結合多個條件
collection =db.website
cursor = collection.find(
    {
        "$or":[
            {"email":"test@test.com"},
            {"password":"test"}
        ]
    }
) 

#  因為一次取得多筆資料，所以要用for迴圈將結果印出來ㄖㄘㄨㄝˉ
for doc in cursor:
    print(doc)

3. 由小到大排序:使用sort參數
語法: 集合.find(篩選條件,sort=排序方式)

collection = db.website
cursor = collection.find({},sort=[
    ("level",pymongo.ASCENDING)
])

4. 由大到小排序:使用sort參數
語法: 集合.find(篩選條件,sort=排序方式)

collection = db.website
cursor = collection.find({},sort=[
    ("level",pymongo.DESCENDING)
])

"""