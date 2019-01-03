# --*--coding:utf-8
# Author:cnn
"""文件拷贝"""


class CopyFile(object):
    def __init__(self, src_path, dest_path):
        self.src_path = src_path
        self.dest_path = dest_path

    def read_file(self):
        file = open(self.src_path, "r", encoding="utf8")
        sum_text = ""
        while True:
            text = file.readline()
            if not text:
                break
            sum_text += text
        file.close()
        return sum_text

    def write_file(self):
        text = self.read_file()
        file = open(self.dest_path, "a", encoding="utf8")
        file.write(text)
        file.close()


if __name__ == "__main__":
    # read=CopyFile("README.txt")
    # text=read.read_file()
    # print(text)
    copy = CopyFile("write.txt", "dest.txt")
    copy.write_file()
