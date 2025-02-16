def example_function():
    try:
        num = int(input("输入一个数字："))
        result = 10 / num
        print(f"10 除以 {num} 得到的结果是：{result}")
    except ValueError:
        print("输入错误，请输入数字！")
    except ZeroDivisionError:
        print("不能除以 0！")
    except Exception as e:
        print(f"出现未知错误：{e}")
    else:
        # 程序正常执行
        print("程序正常执行！")
    finally:
        # 无论是否出现异常，都会执行 finally 块中的代码
        print("程序执行结束！")


if __name__ == '__main__':
    example_function()
