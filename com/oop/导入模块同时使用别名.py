#--*--coding:utf-8
#Author:cnn
#从包导入模块
#from com.oop import model_test_01 as ModelTest #as MT 别名
#从模块中导入部分工具
from com.oop.model_test_01 import  Hello
#模块名.工具
# ModelTest.say_hello()
# print(ModelTest.model_01)
#工具名直接使用
hello=Hello()
print(hello.name)
