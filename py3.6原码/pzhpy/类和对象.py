class Dog():
    """模拟狗"""

    def __init__(self, name, age):
        """构造函数"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟蹲下"""
        print(self.name.title() + "现在坐下!")

    def roll_over(self):
        """模拟打滚"""
        print(self.name.title() + "打滚！")

my_dog = Dog('zll', 3)

print("狗叫" + my_dog.name.title() + '.')
print(my_dog.name.title() + '有' + str(my_dog.age) + '岁了')

my_dog.sit()
my_dog.roll_over()

my_dog2 = Dog('zlh', 2)

print("狗叫" + my_dog2.name.title() + '.')
print(my_dog2.name.title() + '有' + str(my_dog2.age) + '岁了')

my_dog2.sit()
my_dog2.roll_over()
