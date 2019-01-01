# --*--coding:utf-8
# Author:cnn
def refence(num):
    # pass
    print("在函数内部[%d]的内存地址为[%d]" % (num, id(num)))

#定义一个变量a
a = 10
# 内存地址本质上是数字
print("a的内存地址为[%d]" % id(a))
refence(a)