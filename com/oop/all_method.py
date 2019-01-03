# --*--coding:utf-8
# Author:cnn
class Game(object):
    # 定义一个类属性
    top_score = 0

    @staticmethod
    def show_help():
        """静态方法"""
        print("提示信息:让僵尸进门")

    @classmethod
    def show_top_score(cls):
        """
        类方法
        :return:
        """
        print("历史记录:%d" % cls.top_score)

    def __init__(self, name):
        self.name = name

    def start_game(self):
        """
        实例方法
        :return:
        """
        print("%s开始游戏啦..." % self.name)
        Game.top_score=10


if __name__ == "__main__":
    # 显示帮助信息
    Game.show_help()
    # 显示历史分数
    Game.show_top_score()
    # 玩家开始玩游戏
    game = Game("小花")
    game.start_game()
    #print(Game.top_score)
    Game.show_top_score()