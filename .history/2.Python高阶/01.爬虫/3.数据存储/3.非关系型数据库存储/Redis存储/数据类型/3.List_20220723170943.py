from redis_default import con

con.lpush('num1', '1', 2, 'kx', 1.2)  # 从左存储列表多种数据类型
print(con.lrange('num1', 0, -1))  # 获取列表中的数据切片取出
con.rpush('num2', '1', 2, 'kx', 1.2)  # 从右存储列表多种数据类型
print(con.lrange('num2', 0, -1))
print(con.llen('num1'))  # 获取列表的长度
con.




con.delete('num1', 'num2')
