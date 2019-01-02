# --*--coding:utf-8
# Author:cnn
class Parent(object):
    def __init__(self, name):
        self.name = name
        self.__age = 10

    def __secret(self):
        print("%s,%d" % (self.name, self.__age))

    def inter(self):
        self.__secret()


class Sub(Parent):
    pass


sub = Sub("嘿嘿")
print(sub.name)
# 子类不能访问父类的私有属性和方法
# print(sub.__age)
# sub.__secret()
sub.inter()
