#--*--coding:utf-8
#Author:cnn
"""输出字符串出现频率最高的字母"""
str="aAsmr3idd4bgs7Dlsf9eAF"
dict_list=([(x,str.count(x))for x in set(str)])
print(dict_list)
#取出列表中每个元素的第二个键值，并使用从大到小的排序
dict_list.sort(key = lambda k:k[1],reverse=True)