# --*--coding:utf-8
# Author:cnn

#字典是无序的数据集合
# key要唯一,数字,字符串,元组
allen={
    "name":"allen",
    "age":34,
    "height":1.96,
    "number":20,
    "gender":True
}
print(allen)
print(allen.keys())
print(allen.values())
#向字典中新增内容，如果key不存在会新增,如果key存在,则修改内容
allen["weight"]=160
print(allen)
print(allen.keys())
print(allen.values())
#修改
allen["age"]=21
print(allen)
print(allen.keys())
print(allen.values())
#删除
allen.pop("age")
print(allen)
print(allen.keys())
print(allen.values())


