a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = (1, 2, 3)
print(a, b, c)
a, b, c = [1, 2, 3]
print(a, b, c)
a, b, c = (1, 2, 3, 4)
print(a, b, c)  # 报错
a, b, c = [1, 2, 3, 4]
print(a, b, c)  # 报错

# 1.添加
# 1.1 append() 在列表末尾添加新的对象
# 1.2 extend() 在列表末尾一次性追加另一个序列中的多个值
# 1.3 insert() 在指定位置插入一个新的对象

# 2.删除
# 2.1 remove() 删除列表中的一个元素,参数为元素值
# 2.2 pop() 删除列表中的一个元素,参数为索引值,默认删除最后一个元素
# 2.3 del 可以删除一个列表,也可以删除一个列表中的一个元素

# 3.切片
# 列表,元组,字符串都可以使用切片操作,因为它们都属于序列类型
