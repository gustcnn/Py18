#--*--coding:utf-8
#Author:cnn
for gl_num in [1, 2, 3]:
    print(gl_num)
else:
    print("会执行吗?")
print("循环结束.")
#当for循环体内部使用break,else里面的内容不会执行
for gl_num in [1, 2, 3]:
    print(gl_num)
    if gl_num ==2:
        break
else:
    print("会执行吗?")
print("循环结束.")