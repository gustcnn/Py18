# --*--coding:utf-8
# Author:cnn
"""单例设计模式"""


class MusicPlayer(object):
    #类变量,初始化标识
    init_flag=False
    # pass
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(MusicPlayer, cls).__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name
        #标识为False的时候进行初始化,初始化后,修改标识为True,这样控制只初始化一次
        if MusicPlayer.init_flag==False:
            print("初始化")
            MusicPlayer.init_flag=True


if __name__ == "__main__":
    wangyi = MusicPlayer("网易云音乐")
    print(id(wangyi))
    qq = MusicPlayer("QQ音乐 ")
    print(id(qq))
