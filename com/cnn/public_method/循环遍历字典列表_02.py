# --*--coding:utf-8
# Author:cnn
students = [{"name": "阿杜"},
            {"name": "勒布朗"},
            {"name": "禾斗匕匕"}]
find_name="勒布朗01"
#find_name="勒布朗"
for stu_info in students:
    print(stu_info)
    if stu_info["name"]==find_name:
        print("找到了%s"%find_name)
        break
else:
    #for循环所有内容都执行完毕,没有匹配到内容,给予统一的提示
    print("抱歉没有找到%s"%find_name)
print("循环结束.")
