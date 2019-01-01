# --*--coding:utf-8
# Author:cnn
# 缺省参数,定义时给定参数值,如果没有传入,就是默认值,传入了,就是给定值,缺省参数需要放在未缺省参数后面

def  demo(name, gender=True):
    """
    :param name: 姓名
    :param gender: True表示男生,False表示女生
    :return:
    """
    gender_text = "男生"
    # 如果不是男生,修改name_text值
    if not gender:
        gender_text = "女生"
    print("姓名:%s,性别:%s" % (name, gender_text))

#在指定缺省参数默认值时，应该使用最常见的值做为默认值
demo("kobe")
demo("希拉里",gender=False)
