# --*--coding:utf-8
# Author:cnn
'''
姓名:小强
年龄:18岁
性别:男
身高:1.80米
体重:80公斤
'''
name = "小强" #str
age = 18 #int
#sex = "男"
gender=True #bool类型
height = 1.80 #float类型
weight = 80.0 #float


def print_info():
    print("个人信息".center(50, "-"))
    print("姓名:" + name)
    print("年龄:" + str(age))
    print("性别:" + str(gender))
    print("身高:" + str(height))
    print("体重:" + str(weight))


if __name__ == "__main__":
    print_info()
