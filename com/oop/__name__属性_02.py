#--*--coding:utf-8
#Author:cnn
#--*--coding:utf-8
#Author:cnn
def say_hello():
    print("hello,hello")
    #在模块下__name__永远是 __main__
    print(__name__)
#下面代码import包的时候,不会被执行
if __name__=="__main__":
    say_hello()
    print("gust 写的代码")



