#--*--coding:utf-8
#Author:cnn
"""去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），
并且重新输出一个排序后的字符 串。（
保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）"""
str="aAsmr3idd4bgs7Dlsf9eAF"
str_new=""
for i in range(0,len(str)):
    if str[i].isalpha():#判断字符是字母
        str_new+=str[i]
print(str_new)
str_list=[]
for c in str_new:
    str_list.append(c)
str_list.sort()
print(str_list)
