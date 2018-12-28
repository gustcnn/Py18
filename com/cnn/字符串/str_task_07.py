#--*--coding:utf-8
#Author:cnn
"""请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False"""
str = "aAsmr3idd4bgs7Dlsf9eAF"
info="boy"
def isBoy(str,info):
    flag=False
    for i in info:
        if i in str:
            flag=True
        else:
            flag=False
    return flag
if __name__=="__main__":
    print(isBoy(str,info))
