#--*--coding:utf-8
#Author:cnn
"""1、有两个整数变量a=6,b=100 2、不使用其它变量,交换两个变量的值"""
def change():
    a=6
    b=100
    return b,a
a,b=change()
print("交换后的a:%d"%a)
print("交换后的b:%d"%b)
