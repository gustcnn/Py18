#--*--coding:utf-8
#Author:cnn
import os

"""统计file.txt文档中，”be” “is” “than” 的出现次数"""
str_be="be"
str_is="is"
str_than="than"
times_be=0
times_is=0
times_than=0
with open("D:/python/script/Py18/files/file.txt","r") as f:
    str=f.read()
    for i in range(0,len(str)):
        if str[i:i+2] in str_be:
            times_be+=1
            # print("索引%d"%i)
            # print(str[i:i+2])
        if str[i:i+2] in str_is:
            times_is+=1
            # print("索引%d" % i)
            # print(str[i:i+2])
        if str[i:i+4] in str_than:
            times_than+=1
            print("索引%d" % i)
            print(str[i:i+4])
        i-=1
print("be出现的次数:%d"%times_be)
print("is出现的次数:%d"%times_is)
print("than出现的次数:%d"%times_than)
