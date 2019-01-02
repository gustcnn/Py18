# --*--coding:utf-8
# Author:cnn

class Bullet:
    """
    子弹类
    """

    def __init__(self, num):
        """
        :param num:子弹数量
        """
        self.num = num


class Gun:
    """
    枪类
    """

    def __init__(self, name):
        self.name = name
        self.bullet= 0  # 初始枪有0发子弹

    def add_bullet(self, bullet):
        """
        装子弹方法
        :param bullet: 子弹
        :return:
        """
        self.bullet += bullet

    def shoot(self, bullet):
        """
        发射子弹方法
        :return:
        """
        if self.bullet<bullet:
            print("没有足够的子弹了")
            return
        else:
            self.bullet -= bullet

    def __str__(self):
        return "枪:%s\n子弹:%d" % (self.name, self.bullet)


if __name__ == "__main__":
    bullet = Bullet(20)
    gun = Gun("AK47")
    gun.add_bullet(bullet.num)
    print(gun)
    gun.shoot(20)
    print(gun)
