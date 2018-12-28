#--*--coding:utf-8
#Author:cnn
hello_str="hello python"
#判断是否以某个字符开头
print("以hello开头:%s"%hello_str.startswith("hello"))
#判断以某个字符结尾
print("以python结尾:%s"%hello_str.endswith("python"))
#查找子串,返回子串开始的索引
print("子串索引为:%s"%hello_str.find("on"))
print(hello_str.find("abc"))
#替换字符串,不会修改原来的字符串
hello_str_new=hello_str.replace("python","world")
print(hello_str)
print(hello_str_new)