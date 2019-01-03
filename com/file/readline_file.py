# --*--coding:utf-8
# Author:cnn
file = open("README.txt", "r", encoding="utf8")
while True:
    text = file.readline()
    # 判断是否读取到内容,如果未读取到,就退出循环
    if not text:
        break
    print(text)
file.close()
