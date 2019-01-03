# --*--coding:utf-8
# Author:cnn
"""文件拷贝"""


class CopyFile(object):
    def __init__(self, src_path, dest_path):
        self.src_file = open(src_path, "r", encoding="utf8")
        self.dest_file = open(dest_path, "a", encoding="utf8")

    def write(self):
        # 循环,一行一行的读取
        while True:
            text = self.src_file.readline()
            if not text:
                break
            # 将读取的内容一行一行的写入文件
            self.dest_file.write(text)
        if self.dest_file != None:
            self.dest_file.close()
        if self.src_file != None:
            self.src_file.close()


if __name__ == "__main__":
    # read=CopyFile("README.txt")
    # text=read.read_file()
    # print(text)
    copy = CopyFile("README.txt", "dest.txt")
    copy.write()
