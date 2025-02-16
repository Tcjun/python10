class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def bark(self):
        print("汪汪叫---")


class Cat(Animal):
    def meow(self):
        print("喵喵叫---")


class XiaoTianQuan(Dog):
    def bark(self):
        print("woowoo叫---")


if __name__ == '__main__':
    xiaotian = Dog() 
    xiaotian.bark()
    xiaoxiaotian = XiaoTianQuan()
    xiaoxiaotian.bark()
