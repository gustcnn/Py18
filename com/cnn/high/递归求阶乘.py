#--*--coding:utf-8
#Author:cnn
"""递归:自己调用自己"""
def add(num):
    if num==0 or num==1:#递归出口
        return 1
    else:
        return num*add(num-1)#递归体
result=add(4)
print(result)