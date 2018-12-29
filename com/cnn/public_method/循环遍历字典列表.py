# --*--coding:utf-8
# Author:cnn
students = [{"name": "阿杜"},
            {"name": "勒布朗"},
            {"name": "禾斗匕匕"}]
find_name="勒布朗"
for stu_info in students:
    print(stu_info)
    for key in stu_info:
        if stu_info[key]==find_name:
            print("找到了%s"%find_name)
            break
    #break
else:
    print("嘿嘿")
print("循环结束.")
