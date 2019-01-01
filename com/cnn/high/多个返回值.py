#--*--coding:utf-8
#Author:cnn
def measure():
    """
    多个返回值,用元组
    :return:
    """
    print("测量开始...")
    #温度
    measure=39
    #湿度
    wetness=50
    print("测量结束...")
    return (measure,wetness)
result=measure()
print(result)
result_measure=result[0]
result_wetness=result[1]
print(result_measure)
print(result_wetness)
#如果返回值是元组,并且希望单独处理数据,可以使用多个变量接收
gl_measure,gl_wetness=measure()
print(gl_measure)
print(gl_wetness)