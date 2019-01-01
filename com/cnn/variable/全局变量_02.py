# --*--coding:utf-8
# Author:cnn
gl_num=10  # 定义一个全局变量

#num=10
def demo3():
    #希望修改全局变量的值,python中不允许直接修改全局变量的值
    num = 12
    print("demo3中使用全局变量:%d" % num)


demo3()
print("函数外部使用全局变量:%d" % gl_num)
