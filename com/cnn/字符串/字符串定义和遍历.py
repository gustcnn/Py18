#--*--coding:utf-8
#Author:cnn
str1="hello python"
str2="我的爱好是'体育'"
#循环遍历
for c in str1:
    print(c,end="")
print()
for c in str2:
    print(c,end="")
print()
#取值和取索引
print(str1[0])
print(str1[6:len(str1)])
print(str1.index("e"))
print(str1.index("py"))
#统计字符串的长度
le=len(str1)
print("字符串的长度:%d"%le)
#某个子串出现的次数
times=str1.count("l")
print("l出现的次数为:%d"%times)