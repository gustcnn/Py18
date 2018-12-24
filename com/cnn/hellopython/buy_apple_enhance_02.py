# --*--coding:utf-8
# Author:cnn
'''
交互式输入苹果价格和购买斤数,输出购买苹果所需总金额
'''
# 控制台输入并强转为float类型,减少变量的个数
price = float(input("请输入苹果单价>>>:"))
weight = float(input("请输入购买苹果的重量>>>:"))
money = price * weight
print("总金额:" + str(money))
