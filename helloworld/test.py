def set_func(func):
    print("---开始进行装饰")

    def call_func(a):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        func(a)

    return call_func


@set_func  # 相当于 test1 = set_func(test1)
def test1(num):
    print("-----test1----%d" % num)


if __name__ == '__main__':
    test1(10)
# @set_func  # 相当于 test2 = set_func(test2)
# def test2(num):
#     print("-----test2----%d" % num)
