#--*--coding:utf-8
#Author:cnn
#str="1.1"
#str="1"
# str="(1)"
# str="\u00b2"#unicode字符串
str="一"
print(str)
#判断包含数字,但都不能判断小数
print(str.isdigit())
print(str.isdecimal())
print(str.isnumeric())