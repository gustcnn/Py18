#--*--coding:utf-8
#Author:cnn
import random
fist=int(input("请输入您要输入的拳头>>>:"))
computer_random_fist=random.randint(1,3)
if fist==1 and computer_random_fist==2:
    print("石头胜剪刀.")
elif fist==3 and computer_random_fist==3:
    print("布胜石头.")
elif fist==2 and computer_random_fist==1:
    print("剪刀剩布.")
else:
    print("sorry.")