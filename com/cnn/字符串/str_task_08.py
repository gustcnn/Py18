#--*--coding:utf-8
#Author:cnn
"""输出字符串出现频率最高的字母"""
str="aAsmr3idd4bgs7Dlsf9eAF"
times=0
str_new=""
for c in str:
    if c.isalpha():
        str_new+=c
dict={}
dict_list=[]
for c in str_new:
    #dict[c]=str_new.count(c)
    dict_list.append({c:str_new.count(c)})
print(dict_list)


