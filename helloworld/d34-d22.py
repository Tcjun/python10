print("******多继承使用super().__init__ 发生的状态******")


class Parent(object):

    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent 的init 开始被调用')
        self.name = name
        print('parent 的init 结束被调用')


class Son1(Parent):

    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1 的init 开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用  不定长参数，接受参数
        print('Son1 的init 结束被调用')


class Son2(Parent):

    def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2 的init 开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2 的init 结束被调用')


class Grandson(Son1, Son2):

    def __init__(self, name, age, gender):
        print('Grandson 的init 开始被调用')
        super().__init__(name, age, gender)  # 调用父类的init方法
        print('Grandson 的init 结束被调用')


print("******多继承使用super().__init__ 发生的状态******\n\n")
print(Grandson.__mro__)
gs = Grandson('Grandson', 20, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)
print("******多继承使用super().__init__ 发生的状态******\n\n")
