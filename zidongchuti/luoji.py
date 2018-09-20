# python 3.62
# utf-8

import random

# 自动问答机


class zidongwendaji():

    """正则表达式练习"""

    def __init__(self, recodes, right=0, error=0):
        """字典，正确次数，错误次数，字典key列表"""
        self.recodes = recodes
        self.right = right
        self.error = error
        self.key_list = []
        #用于检测后退出循环
        self.breaks = False

    def recodes_key_list(self):
        """生成一个recodes的key列表"""
        for key in self.recodes.keys():
            self.key_list.append(key)

    def goceshi(self):
        """出题机"""
        # recodes的索引列表key_list，生成的随机索引号
        recodeskeyNum = random.randint(0, len(self.key_list) - 1)
        # 根据随机索引号，找到索引内容
        randomkey = self.key_list[recodeskeyNum]
        # 打印索引，输入符号，根据索引内容找到recodes值，与输入的符号进行比较
        recode = input("\n含义：" + randomkey + "\n")
        if recode == self.recodes[randomkey]:
            print("答案正确")
            self.right += 1

        elif recode == "Quit":
            self.breaks = True

        else:
            print("答案错误")
            print("正确答案为：" + self.recodes[randomkey])
            self.error += 1

    def right_error(self):
        # 正确率计算
        print("正确：%d 道题\n错误：%d 道题" % (self.right, self.error))
        print("输入'Quit'退回选择界面。")
        print(">>>>>>>>>>>>>>>>")
