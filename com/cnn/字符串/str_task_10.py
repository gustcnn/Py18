#--*--coding:utf-8
#Author:cnn
"""已知 a = [1,2,3,6,8,9,10,14,17],请将该list转换为字符串"""
a = [1,2,3,6,8,9,10,14,17]
str_new=""
for c in a:
    str_new+=str(c)
print(str_new)