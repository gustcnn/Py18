# --*--coding:utf-8
# Author:cnn
# 元组通常存储不同类型的数据
info_tuple = ("张三", 18, 1.75,"张三")
#取值
print(info_tuple[0])
#取索引
print(info_tuple.index("张三"))
#元素在元组中出现的次数
print(info_tuple.count("张三"))
#遍历元组
for info in info_tuple:
    print(info)

# 定义一个空元组
empty_tuple=()
print(type(empty_tuple))

#定义包含一个元素的元组
single_tuple=(5,)
print(type(single_tuple))

#统计元组中包含的元素个数
print("元组中包含的元素个数为:"+str(len(info_tuple)))
