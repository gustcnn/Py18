#--*--coding:utf-8
#Author:cnn
def demo1():
    num=int(input("请输入一个整数:"))
    result=8/num
    return reslut
def demo2():
    return demo1()

#利用异常的传递性,在主程序捕获异常
try:
    demo2()
except Exception as reslut:
    print(reslut)