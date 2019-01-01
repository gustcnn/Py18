# --*--coding:utf-8
# Author:cnn
def add(num):
    """
    求1~num之和
    :param num: 给定数
    :return:
    """
    sum = 0
    if num == 1:
        return 1
    else:
        sum += num + add(num - 1)
        return sum


result = add(100)
print(result)
