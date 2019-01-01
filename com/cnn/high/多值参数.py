# --*--coding:utf-8
# Author:cnn
# 参数不确定
def demo(num, *args, **kwargs):
    """
    :param num:
    :param args: 接收元组
    :param kwargs: 接收字典
    :return:
    """
    # pass
    print(num)
    print(args)
    print(kwargs)
demo(1)
"""
1
(2, 3)
{'name': 'cnn', 'age': 18, 'gender': '女'}
"""
demo(1, 2, 3, name="cnn", age=18,gender="女")
