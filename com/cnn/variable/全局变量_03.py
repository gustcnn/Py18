# --*--coding:utf-8
# Author:cnn
gl_num = 10
print("修改前的num:%d" % gl_num)


def demo4():
    # 表名此num为全局变量的num
    global gl_num
    # 修改全局变量的值
    gl_num = 100
    num=99
    print("在demo4中修改全局变量:%d" % gl_num)
    print("局部变量:%d"%num)


demo4()
print("函数外部使用全局变量:%d" % gl_num)
