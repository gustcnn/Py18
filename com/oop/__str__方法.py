# --*--coding:utf-8
# Author:cnn
# --*--coding:utf-8
# Author:cnn
class Cat:
    # 类的属性
    # name = ""
    # color = ""

    def __init__(self, name, color):
        """
        初始化方法中设置属性,为属性设置初始值
        :param name: 名字
        :param color: 颜色
        """
        # 使用self.属性名=属性初始值,name属性名就是类具有的属性了
        self.name = name
        self.color = color

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __str__(self):
        """
        重写__str__方法
        :return:
        """
        # return self.name
        return "我是小猫[%s]" % self.name


if __name__ == "__main__":
    cat = Cat("小花", "黑白")
    cat.eat()
    # print(cat.name)
    # print(cat.color)
    # 未重写__str__方法前,打印输出<__main__.Cat object at 0x000000000252A208>
    # print(cat)
    # 重写__str__方法后,打印对象,输出__str__方法的返回值
    print(cat)
