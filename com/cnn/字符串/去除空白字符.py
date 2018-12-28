#--*--coding:utf-8
#Author:cnn
str=" \r\n七律·人民解放军占领南京\
毛泽东\
钟山风雨起苍黄，\
百万雄师过大江。\
虎踞龙盘今胜昔，\
天翻地覆慨而慷。\
宜将剩勇追穷寇，\
不可沽名学霸王。\
天若有情天亦老，\
人间正道是沧桑。"
#去除字符串前后的空白符
str_strip=str.strip(" \r\n")
print("去除前后空白符后的字符串为:%s"%str_strip)
#去除字符串左边的空白符
str_lstrip=str.lstrip(" \r\n")
print(str_lstrip)
#去除字符串右边的空白符
str_rstrip=str.rstrip(" \r\n")
print(str_rstrip)