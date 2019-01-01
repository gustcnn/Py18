#--*--coding:utf-8
#Author:cnn
#全局变量
gl_num=10
def demo1():
    print("demo1中使用全局变量:%d" % gl_num)
def demo2():
    #局部变量
    num=99
    print("demo2中定义一个局部变量:%d"%num)

demo1()
demo2()

