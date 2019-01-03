# --*--coding:utf-8
# Author:cnn
class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        print("重写new方法,分配内存空间")
        isinstance=super().__new__(cls)#调用父类的__new__方法
        return isinstance

    def __init__(self, name):
        self.name = name
        print("%s播放器" % self.name)
if __name__=="__main__":
    player=MusicPlayer("网易云音乐")
    print(id(player))

