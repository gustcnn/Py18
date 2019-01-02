# --*--coding:utf-8
# Author:cnn
# 多态
class Dog(object):
    """
    多态:要有继承,父类方法重写,父类引用指向之类对象
    """
    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s 蹦蹦跳跳的玩耍." % self.name)


class XiaoTianQuan(Dog):
    def play(self):
        print("%s 飞到天上去玩耍." % self.name)


class Person(object):
    def __init__(self,name):
        self.name=name
    def play_with_dog(self,dog):
        print("%s 和 %s 快乐的玩耍."%(self.name,dog.name))
        dog.play()
if __name__=="__main__":
    person=Person("小黄")
    #dog=Dog("旺财")
    dog=XiaoTianQuan("飞天旺财")
    person.play_with_dog(dog)
