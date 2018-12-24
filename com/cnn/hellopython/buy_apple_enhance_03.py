# --*--coding:utf-8
# Author:cnn
'''
格式化输出
%d 整型
%f 浮点型
%s 字符串
'''
price = float(input("请输入苹果单价>>>:"))
weight = float(input("请输入购买苹果的重量>>>:"))
money = price * weight
#%.2f小数点后2位
print("总金额:%.2f=%.2f*%.2f"%(money,price,weight))
