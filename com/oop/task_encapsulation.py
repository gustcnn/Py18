# --*--coding:utf-8
# Author:cnn
"""
练习封装
需求：
1、小明体重75.0公斤
2、小明每次跑步会减肥0.5公斤
3、小明每次吃东西体重增加1公斤
"""


class Person:
    def __init__(self, name, weight):
        """
        初始化方法
        :param name: 名字
        :param weight: 体重
        """
        self.name = name
        self.weight = weight

    def eat(self):
        """
        吃东西方法
        :return:
        """
        self.weight += 1  # 每吃一次东西,体重增加1公斤
        print("%s是吃货,吃完了再减肥."%self.name)
        return self.weight

    def run(self):
        """
        跑步方法,每跑一次步,体重减少0.5公斤
        :return:
        """
        print("%s爱跑步,跑步锻炼身体"%self.name)
        self.weight -= 0.5
        return self.weight

    def __str__(self):
        return "我叫%s，体重是%.2f公斤" % (self.name, self.weight)


if __name__ == "__main__":
    xiaoming = Person("小明", 75)
    # 小明的初始体重
    print(xiaoming)
    xiaoming.eat()
    # 吃东西后小明的体重
    print(xiaoming)
    xiaoming.run()
    # 吃完东西,再跑完步之后小明的体重
    print(xiaoming)
    xiaomei=Person("小美",45)
    xiaomei.run()
    print(xiaomei)
    xiaomei.eat()
    print(xiaomei)
