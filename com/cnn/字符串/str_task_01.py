# --*--coding:utf-8
# Author:cnn
"""将a字符串的大写改为小写，小写改为大写"""
str = "aAsmr3idd4bgs7Dlsf9eAF"
st = ""
# 循环遍历字符串,判断每个字符是大写还是小写,是大写转换为小写,是小写转换为大写
for c in str:
    if c.isupper():
        st += c.lower()
    if c.islower():
        st += c.upper()
print(st)
