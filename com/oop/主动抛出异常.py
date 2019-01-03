#--*--coding:utf-8
#Author:cnn
"""
1、提醒用户输入密码
2、判断密码长度 >8正常运行 <8抛出异常
"""
def input_password():
    pwd=input("请输入密码:")
    if len(pwd)>=8:
        for i in pwd:
            if i not in ["_","1"]:
                ex8=Exception("密码复杂度不够.")
                raise  ex8
        return pwd
    #长度不够8,主动抛出异常
    #1、创建异常对象
    ex=Exception("密码长度不够")
    #使用raise抛出异常
    raise ex

#捕获异常
try:
    password=input_password()
    print("输入的密码为:%s"%password)
except Exception as result:
    print(result)

