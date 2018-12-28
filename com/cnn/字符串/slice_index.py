# --*--coding:utf-8
# Author:cnn
str = "hello python"
#截取从2-5位置的字符串
str_2_5=str[2:6]
print("截取2-5位置的字符串:%s"%str_2_5)
#截取从2-末尾的字符串
str_2_len=str[2:len(str)]
print("截取2-末尾位置的字符串:%s"%str_2_len)
#截取开始~5位置的字符串
str_start_5=str[0:6]
print("截取开始~5位置的字符串:%s"%str_start_5)
#截取完整字符串
#str_full=str[0:len(str)]
str_full=str[:]
print("截取完整字符串:"+str_full)
#从开始位置,每个一个字符截取字符串
str_0_1=str[0:len(str):2]
print("从开始位置,每个一个字符截取字符串:"+str_0_1)
#从索引1开始,每隔一个取一个
str_1_1=str[1:len(str):2]
print("从索引1开始,每隔一个取一个:"+str_1_1)
#截取从2~末尾-1的字符串
str_2_len_1=str[2:len(str)-1]
print("截取从2~末尾-1的字符串:"+str_2_len_1)
#截取字符串末尾两个字符
str_1_2=str[-1:-3:-1]
print("截取字符串末尾两个字符:"+str_1_2[::-1])
#字符串的逆序
# str_reverse=str[-1:-len(str)-1:-1]
str_reverse=str[-1::-1]
print(str_reverse)
