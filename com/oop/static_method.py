# --*--coding:utf-8
# Author:cnn
class Dog(object):
    # 类属性
    count = 0
    """
    静态方法,使用staticmethod装饰器
    """

    @staticmethod
    def run():
        #不访问类属性和对象属性
        print("小狗在跑。。。")

    def __init__(self, name):
        self.name = name  # 实力属性
        Dog.count += 1

    @classmethod
    def show_run_dog(cls):
        # Dog.run()
        print("在跑的狗的数量:%d" % Dog.count)


if __name__ == "__main__":
    xiaohuang = Dog("")

if __name__ == "__main__":
    #静态方法调用类名.静态方法
    Dog.run()
    xiaohuang = Dog("小黄")
    xiaohua = Dog("小花")
    Dog.show_run_dog()
