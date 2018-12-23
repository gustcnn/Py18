# --*--coding:utf-8
# Author:cnn
'''
姓名:小强
年龄:18岁
性别:男
身高:1.80米
体重:80公斤
'''


class Person:
    name = "小强"
    age = 18
    sex = "男"
    height = 1.80
    weight = 80

    def print_person_info(self):
        print("个人信息".center(50, "-"))
        print("姓名:" + self.name)
        print("年龄:" + str(self.age))
        print("性别:" + self.sex)
        print("身高:" + str(self.height))
        print("体重:" + str(self.weight))


if __name__ == "__main__":
    person=Person()
    person.print_person_info()
