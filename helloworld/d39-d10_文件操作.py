f = open('hello.txt', 'w+', encoding='utf-8')  # 打开文件，如果文件不存在则创建，如果存在则覆盖

f.write('Hello, world!\n')  # 写入内容
f.write('你好，世界！\n')

# f.seek(0)  # 移动文件指针到开头
# text = f.read()  # 读取全部内容
# print(text)

f.seek(5)  # 移动文件指针到开头
while True:
    line = f.readline()  # 读取一行内容
    if not line:
        break
    print(line.strip())  # 去掉换行符

# f.seek(0)  # 移动文件指针到开头
#
# lines = f.readlines()  # 读取所有内容并按行分割
# for line in lines:
#     print(line.strip())

f.close()  # 关闭文件
