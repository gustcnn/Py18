# --*--coding:utf-8
# Author:cnn
from com.oop.gun_bullet import Gun


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None#新兵没有枪
    def add_gun(self,gun):
        self.gun=gun
    def fire(self, bullet):
        if self.gun is None:#is 比较内存地址 ==比较值
            print("新兵没有枪,请申请.")
            return
        if self.gun.bullet >= bullet:
            self.gun.bullet -= bullet
        else:
            print("枪:%s没有子弹了" % self.gun.name)
            return

    def __str__(self):
        if self.gun is None:
            return ""
        else:
            return str({"士兵": self.name, "枪": self.gun.name, "子弹": self.gun.bullet})


if __name__ == "__main__":
    # pass
    gun = Gun("AK47")
    gun.add_bullet(20)
    # print(gun.bullet)
    soldier = Soldier("许三多")
    print(soldier)
    soldier.add_gun(gun)
    soldier.fire(19)
    print(soldier)
