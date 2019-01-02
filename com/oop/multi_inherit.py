# --*--coding:utf-8
# Author:cnn
class A(object):
    def test(self):
        print("test...")

    def demo(self):
        print("A demo...")


class B(object):
    def demo(self):
        print("B demo...")


class C(A, B):
    """
    多继承可以让子类拥有多个父类的的属性和方法,切记多个父类中不要有相同的属性名或者方法
    """
    pass


if __name__ == "__main__":
    c = C()
    c.test()
    c.demo()
    # method resolution order 方法执行顺序
    print(C.__mro__)
