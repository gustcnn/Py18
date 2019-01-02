# --*--coding:utf-8
# Author:cnn
class Dog:
    color = ""
    name = ""

    def dog_info(self, name, color):
        self.name = name
        self.color = color
        print("一只%s颜色的狗狗叫%s"%(self.color,self.name))
    def shout(self):
        """
        狗叫
        :return:
        """
        #pass
        print("%s看见生人叫"%self.name)

    def wag_tail(self):
        """
        狗摇尾巴
        :return:
        """
        #pass
        print("%s看见家人摇尾巴"%self.name)
if __name__=="__main__":
    yellow=Dog()
    yellow.dog_info("大黄","黄色")
    yellow.shout()
    yellow.wag_tail()