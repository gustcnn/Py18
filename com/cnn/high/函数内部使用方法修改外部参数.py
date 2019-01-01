#--*--coding:utf-8
#Author:cnn
"""函数参数是可变类型,使用方法修改,会改变外部数据"""
def demo(num_list):
    print("函数内部代码")
    num_list.append(9)
    print(num_list)
    print("函数内部代码执行完毕")
gl_num_list=[1,2,3]
demo(gl_num_list)
print(gl_num_list)