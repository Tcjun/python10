def input_password():
    # 1. 提示用户输入密码
    pwd = input("请输入密码：")
    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
        # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象- 可以使用错误信息字符串作为参数
    raise Exception("密码长度不够")
    # 2> 主动抛出异常
    # raise ex
    # 提示用户输入密码


# try:
#     print(input_password())
# except Exception as result:
#     print(result)
def assert_example():
    try:
        assert 1 == 2, "1 不等于 2"
        print("1 等于 2")
    except AssertionError as result:
        print(result)


if __name__ == '__main__':
    assert_example()
