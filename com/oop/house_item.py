#--*--coding:utf-8
#Author:cnn
class HouseItem:
    """
    家具类
    """
    def __init__(self,name,area):
        """
        初始化
        :param name: 家具名字
        :param area: 家具占地面积
        """
        self.name=name
        self.area=area

    def __str__(self):
        return "[%s]占地面积%.2f"%(self.name,self.area)
if __name__=="__main__":
    bed=HouseItem("床",4)
    chest=HouseItem("衣柜",2)
    table=HouseItem("桌子",1)
    print(bed)
    print(chest)
    print(table)