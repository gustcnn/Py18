#--*--coding:utf-8
#Author:cnn
"""类属性:
    1、记录跟类相关的特征的
    2、不记录跟对象相关的特征
    3、使用类名.属性名 调用
"""
class Tool(object):
    #类属性
    count=0
    def __init__(self,name):
        #对象属性,使用self.属性名调用
        self.name=name
        Tool.count+=1
if __name__=="__main__":
    tool1=Tool("钳子")
    tool2=Tool("手电筒")
    tool3=Tool("螺丝刀")
    print(Tool.count)