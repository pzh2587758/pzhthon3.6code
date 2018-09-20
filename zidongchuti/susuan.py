import random


class susuan(object):

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.num3 = None
        self.right = 0
        self.error = 0
        self.breaksusuan = True

    def digit_add(self):
        self.num1 = random.randint(10, 999)
        self.num2 = random.randint(10, 999)
        self.num3 = self.num1 + self.num2
        print("%d + %d = ?" % (self.num1, self.num2))
        numinput = input("请输入计算结果：")
        if numinput == "Quit":
            self.breaksusuan = False
        elif int(numinput) == self.num3:
            print("计算正确")
            self.right += 1
        else:
            print("计算错误！！")
            print("正确答案为 %d" % self.num3)
            self.error += 1

    def digit_SUB(self):
        self.num1 = random.randint(10, 99)
        self.num2 = random.randint(10, 99)
        if self.num1 > self.num2:
            self.num3 = self.num1 - self.num2
            print("%d - %d = ?" % (self.num1, self.num2))
            numinput = input("请输入计算结果：")
            if numinput == "Quit":
                self.breaksusuan = False
            elif int(numinput) == self.num3:
                print("计算正确")
                self.right += 1
            else:
                print("计算错误！！")
                print("正确答案为 %d" % self.num3)
                self.error += 1
        else:
            pass

    def digit_MUL(self):
        self.num1 = random.randint(10, 99)
        self.num2 = random.randint(10, 99)
        self.num3 = self.num1 * self.num2
        print("%d * %d = ?" % (self.num1, self.num2))
        numinput = input("请输入计算结果：")
        if numinput == "Quit":
            self.breaksusuan = False
        elif int(numinput) == self.num3:
            print("计算正确")
            self.right += 1
        else:
            print("计算错误！！")
            print("正确答案为 %d" % self.num3)
            self.error += 1

    def digit_DIV(self):
        self.num1 = random.randint(10, 99)
        self.num2 = random.randint(10, 99)
        if self.num1 > self.num2:
            self.num3 = self.num1 // self.num2
            print("%d / %d = ?" % (self.num1, self.num2))
            numinput = input("请输入计算结果：")
            if numinput == "Quit":
                self.breaksusuan = False
            elif int(numinput) == self.num3:
                print("计算正确")
                self.right += 1
            else:
                print("计算错误！！")
                print("正确答案为 %d" % self.num3)
                self.error += 1
        else:
            pass

    def right_error(self):
        print("正确: %d 错误: %d" % (self.right, self.error))
        print("输入'Quit'退出循环。\n")
        print(">>>>>>>>>>>>>>>>>")
