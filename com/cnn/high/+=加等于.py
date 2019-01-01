#--*--coding:utf-8
#Author:cnn
def demo(num,num_list):
    print("函数内部代码")
    num+=num
    #num_list使用+=相当于num_list.extend()
    #num_list+=num_list
    #num_list.extend(num_list)
    #列表变量使用+,不会做相加再赋值的操作
    num_list=num_list+num_list
    print(num)
    print(num_list)
    print("函数内部代码执行结束")
num=9
gl_num_list=[1,2,3]
demo(num,gl_num_list)
print(num)
print(gl_num_list)
