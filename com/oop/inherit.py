# --*--coding:utf-8
# Author:cnn
"""继承"""


class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# 狗类继承动物类
class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def sleep(self):
        #使用父类名.父类方法,记得传入self,python3中不推荐使用
        Dog.sleep(self)
        print("站着睡觉.")
    def bark(self):
        super().bark()#调用父类方法
        print("嗷嗷嗷嗷嗷嗷....")
    def fly(self):
        print("飞呀飞呀飞呀.")


if __name__ == "__main__":
    wangcai = XiaoTianQuan()
    wangcai.eat()
    wangcai.run()
    wangcai.drink()
    wangcai.sleep()
    wangcai.bark()
    wangcai.fly()
