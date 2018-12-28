#--*--coding:utf-8
#Author:cnn
poem_str=" 鹅鹅鹅\t\n曲项向天歌\t\r\n白毛浮绿水\r\n红掌拨清波\r\n"
print(poem_str)
#拆分字符串,生成列表
poem_list=poem_str.split()#不填写分隔字符串,任何空白符都可做为分隔字符串\r\t\n
print(poem_list)
#使用空格拼接字符串
poem=" ".join(poem_list)
print(poem)