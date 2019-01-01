# --*--coding:utf-8
# Author:cnn
def demo(name, title=" ", gender=True):
    """
    缺省参数
    :param title: 职位,默认为空
    :param name: 姓名
    :param gender: 性别,默认男生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("姓名:%s,职位:%s,性别:%s" % (name, title, gender_text))


demo("kobe")
# 当有多个缺省参数时,需要传递值给参数,需要指定参数的名字,如下:
demo("lbj", title="mvp")
demo("cnn", title="mvp", gender=False)
