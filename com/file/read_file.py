#--*--coding:utf-8
#Author:cnn
import os
str=os.path.dirname(__file__)
# print(str)
#file=open("README.txt","r",encoding="utf8")
file=open(str+"/"+"README.txt","r",encoding="utf8")
#返回文件所有内容，file.read()，一次性将所有内容加载到内存
text=file.read()
print(text)
print("-"*50)
file.seek(0)
text=file.read()
print(text)
file.close()
