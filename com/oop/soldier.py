# --*--coding:utf-8
# Author:cnn
from com.oop.gun_bullet import Gun


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.Gun = gun

    def fire(self, bullet):
        if self.Gun.bullet >= bullet:
            self.Gun.bullet -= bullet
        else:
            print("枪:%s没有子弹了" % self.Gun.name)
            return

    def __str__(self):
        return str({"士兵": self.name, "枪": self.Gun.name, "子弹": self.Gun.bullet})


if __name__ == "__main__":
    # pass
    gun = Gun("AK47")
    gun.add_bullet(20)
    # print(gun.bullet)
    soldier = Soldier("许三多", gun)
    print(soldier)
    soldier.fire(19)
    print(soldier)
