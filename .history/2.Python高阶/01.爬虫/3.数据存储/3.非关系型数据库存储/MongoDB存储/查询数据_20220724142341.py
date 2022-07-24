import pymongo

myClient = pymongo.MongoClient('mongodb://45.43.61.98:27017/')
my_db = myClient['mydatabase']
my_col = my_db["sites"]

# 1.查询一条数据
print(my_col.find_one(), '_____________')

# 2.查询多条数据
for x in my_col.find():
    print(x)

# 3. 指定id查询数据
print(my_col.find_one({"_id": 3}), '_____________')

# 4. 查询指定字段
print(my_col.find_one({"name": "Zhihu"}), '_____________')

# 5. 查询指定字段值
print(my_col.find_one({"name": "Zhihu"}, {
    "_id": 0,
    "name": 1
}), '_____________')
