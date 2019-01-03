#--*--coding:utf-8
#Author:cnn
#从package import .py
from com.oop import model_test_01
from com.oop import model_test_02
#from com.oop.model_test_01 import *
print(model_test_01.model_01)
#调用 模块名.方法名
model_test_01.say_hello()
hello=model_test_01.Hello()
print(hello)
print(model_test_01.Hello.name)
