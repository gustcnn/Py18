# --*--coding:utf-8
# Author:cnn
class Person:
    name = ""
    age = 0
    height = 0

    def person_info(self, name, age, height):
        """
        初始化信息,并打印
        :param name: 姓名
        :param age: 年龄
        :param height:身高
        :return:
        """
        self.name = name
        self.age = age
        self.height = height
        print("%s今年%d岁,身高%.2f" % (self.name, self.age, self.height))

    def run(self):
        """
        跑步方法
        :return:
        """
        print("%s跑步" % self.name)

    def eat(self):
        """
        吃东西方法
        :return:
        """
        print("%s吃东西" % self.name)


if __name__ == "__main__":
    xiao_mei = Person()
    xiao_ming = Person()
    xiao_ming.person_info("小明", 18, 1.75)
    xiao_ming.run()
    xiao_ming.eat()
    xiao_mei.person_info("小美", 17, 1.75)
    xiao_mei.eat()
