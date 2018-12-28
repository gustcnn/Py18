#--*--coding:utf-8
#Author:cnn
"""去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’"""
str = "aAsmr3idd4bgs7Dlsf9eAF"
#定义一个空列表
str_list=[]
#定义一个空字符串
str_new=""
#循环遍历字符串,如果字符不在列表中,追加到列表
for c in str:
    if c not in str_list:
        str_list.append(c)
print(str_list)
#循环遍历列表,更新字符串
for c in str_list:
    str_new+=c
print(str_new)