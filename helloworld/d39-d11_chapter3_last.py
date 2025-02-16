import os
from time import strftime
from time import gmtime

# file1 = open("hello.txt", 'r', encoding='utf-8')
# file2 = open("world.txt", 'w', encoding='utf-8')

# 获取文件大小
file1_size = os.path.getsize("hello.txt")
print("文件大小为：", file1_size, "字节")

file_info = os.stat("hello.txt")
print("文件信息：", file_info)

print('size {},uid {},mode {:x},mtime {}'.format(file_info.st_size, file_info.st_uid,
                                             file_info.st_mode, file_info.st_mtime))

# 把秒数转为字符串时间
print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))
