#--*--coding:utf-8
#Author:cnn
class Women:
    def __init__(self,name):
        self.name=name
        self.__age=18#私有属性 __属性名
    def __secret(self):#私有方法 两个下划线+方法名
        print("我的姓名%s,年龄%d"%(self.name,self.__age))

if __name__=="__main__":
    xiaofang=Women("小芳")
    ##私有属性和方法在类外不能被使用
    #xiaofang.__secret()
    #伪私有,可以用如下方式访问私有的内容,但是不建议使用
    print(xiaofang._Women__age)