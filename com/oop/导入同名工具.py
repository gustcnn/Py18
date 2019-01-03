#--*--coding:utf-8
#Author:cnn
#当有同名的工具时,可以通过起别名来避免覆盖
from com.oop.model_test_01 import say_hello as model_test_01_say_hello
from com.oop.model_test_02 import say_hello
say_hello()
model_test_01_say_hello()
