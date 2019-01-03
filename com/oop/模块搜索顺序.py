#--*--coding:utf-8
#Author:cnn
import random
#生成0-10之间的随机整数
count=0
while True:
    rand=random.randint(0,10)
    print(rand)
    count+=1
    if count==5:
        break
#查看当前工作目录
print(__file__)
#查看random的路径
print(random.__file__)


