# --*--coding:utf-8
# Author:cnn
class HouseItem:
    """
    家具类
    """

    def __init__(self, name, area):
        """
        初始化
        :param name: 家具名字
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地面积%.2f" % (self.name, self.area)


class House:
    """
    房子类
    """

    def __init__(self, house_type, total_area):
        """
        初始化房子类
        :param house_type: 户型
        :param total_area:总面积
        """
        self.house_type = house_type
        self.total_area = total_area
        self.area = self.total_area
        self.house_item_list = []

    def add_item(self, house_item):
        """
        添加家具
        :param house_item: 家具类
        :return:
        """
        if house_item.area<=self.area:
            #将家具追加到家具列表
            self.house_item_list.append(house_item.name)
            #剩余面积
            self.area -= house_item.area

            print("户型:[%s]\n家具:[%s]\n剩余面积:[%.2f]\n" % (self.house_type, house_item, self.area))
        else:
            print("无法添加")
            return

    def __str__(self):
        return "[%s]户型,剩余面积为[%.2f],家具名称列表:%s" % (self.house_type, self.area,str(self.house_item_list))


if __name__ == "__main__":
    bed = HouseItem("床", 40)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("桌子", 1)
    chair=HouseItem("椅子",0.5)
    # print(bed)
    # print(chest)
    # print(table)
    house = House("两室一厅", 100)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    house.add_item(chair)
    print(house)
