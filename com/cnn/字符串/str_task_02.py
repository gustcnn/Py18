#--*--coding:utf-8
#Author:cnn
"""将a字符串的数字取出，并输出成一个新的字符串"""
str = "aAsmr3idd4bgs7Dlsf9eAF"
str_new=""
for c in str:
    if c.isdecimal():
        str_new+=c
print(str_new)