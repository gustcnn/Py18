# --*--coding:utf-8
# Author:cnn
"""请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典"""
str = "aAsmr3idd4bgs7Dlsf9eAF"
# 定义一个空字典
dict_str = {}
# 循环遍历字符串
for c in str:
    if c.islower():#如果是小写字母,转换为大写字母,更新字符串
        c=c.upper()
        str+=c
    dict_str[c] = str.count(c)
print(dict_str)
