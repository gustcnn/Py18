# --*--coding:utf-8
# Author:cnn
'''
需求:
在超市买7.7斤苹果，每斤苹果6.98元,只要购买苹果,就返现5元
'''
# 苹果单价
price = 6.98
# 苹果斤数
weight = 7.7
# 总额
money = price * weight
#在控制台输出未返现前的总额
print(money)
#输出返现后的总额
money=money-5
print(money)
