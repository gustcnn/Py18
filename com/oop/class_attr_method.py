# --*--coding:utf-8
# Author:cnn
"""
类方法,@classmethod cls
"""


class Tool(object):
    # 类属性
    count = 0

    @classmethod
    def show_tool_count(cls):
        """
        类方法,使用@classmethod装饰器,表名是类方法,方法的第一个参数是cls（class）
        :return:
        """
        print("工具类被调用次数:%d"%cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1
if __name__=="__main__":
    tool1=Tool("斧子")
    tool1=Tool("镰刀")
    tool1=Tool("锤子")
    Tool.show_tool_count()
