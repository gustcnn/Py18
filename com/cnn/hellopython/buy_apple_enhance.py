# --*--coding:utf-8
# Author:cnn
'''
交互式输入苹果价格和购买斤数,输出购买苹果所需总金额
'''
price_str = input("请输入苹果单价>>>:")
price = float(price_str)  # price_str为字符串,使用float()强转为浮点型
weight_str = input("请输入购买苹果的重量>>>:")
weight = float(weight_str)
money = price * weight
print("总金额:" + str(money))
