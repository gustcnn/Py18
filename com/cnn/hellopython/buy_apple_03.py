# --*--coding:utf-8
# Author:cnn
'''
需求:
在超市买7.7斤苹果，每斤苹果6.98元,求总额
'''
def buy_apple(price,weight):
    money=price*weight
    return money
'''
需求:
在超市买7.7斤苹果，每斤苹果6.98元,如果购买的斤数超过5斤,就返现5元
'''
def buy_apple_enhance(price,weight):
    if weight>=5:
        money=price*weight-5
    else:
        money=price*weight
    return money

if __name__=="__main__":
    ba=buy_apple(7.5,5)
    bae=buy_apple_enhance(7.5,5)
    print(ba)
    print(bae)

