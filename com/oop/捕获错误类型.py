#--*--coding:utf-8
#Author:cnn
"""
1、提示用户输入一个整数
2、使用8除以用户输入的整数并且输出
"""
try:
    num=int(input("请输入一个整数:"))
    result=8/num
    print(result)
except ValueError:
    print("请输入一个正确的整数")
except ZeroDivisionError as ze:
    print("0不能作为分母")
except Exception as result:#捕获的错误类型为Exception
    print("未知错误%s"%result)
else:
    print("else,没有出现except")
finally:
    print("finally,无论错误与否，都会执行")
print("game over.")