# --*--coding:utf-8
# Author:cnn
def add(*args):
    """
    求多个参数之和
    :param args:接收元组(多个参数)
    :return:
    """
    sum = 0
    for i in args:
        sum += i
    return sum


result=add(1, 2, 3)
print(result)
