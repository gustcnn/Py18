# --*--coding:utf-8
# Author:cnn
'''
格式化输出
'''
name = "gust"
student_no =1
price = 9.00
weight = 5.0
money = price * weight
scale = 10.00  # 比例
print("我的名字叫%s,请多多关照" % name)
print("我的学号是:%06d" % student_no)#我的学号是:000001
#%0.2f小数点后保留2位
print("苹果单价%.2f/斤,购买了%0.2f斤,总金额%0.2f元" % (price, weight, money))
#输出百分比10.00%
print("比例是:%0.2f%%" % scale)
