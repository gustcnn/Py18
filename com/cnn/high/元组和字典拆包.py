#--*--coding:utf-8
#Author:cnn
def demo(*args,**kwargs):
    """
    多值参数
    :param args: 接收元组
    :param kwargs: 接收字典
    :return:
    """
    print(args)
    print(kwargs)
gl_nums=(1,2,3)
gl_dict={"name":"小凯","age":18}
#运行结果
"""((1, 2, 3), {'name': '小凯', 'age': 18})
{}"""
#demo(gl_nums,gl_dict)
#运行结果
"""(1, 2, 3)
{'name': '小凯', 'age': 18}"""
#使用拆包可以简化字典和元组做为参数
demo(*gl_nums,**gl_dict)