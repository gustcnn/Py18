#--*--coding:utf-8
#Author:cnn
#九九乘法表
for row in range(1,10):
    for column in range(1,row+1):
        print(str(column)+"*"+str(row)+"="+str(row*column)+" ",end="")#end控制换行与否
    print()
