#--*--coding:utf-8
#Author:cnn
def demo01():
    """局部变量:定义在函数内部的变量
    """
    #定义一个局部变量
    num=10
    print("demo01中定义的局部变量%d"%num)
def demo02():
    num=99
    print("demo02中定义的局部变量%d"%num)

demo01()
demo02()