#python3.6
#关于剔除前期已有号码的3D猜测

import random
from randome_one import screen_accuracy

class screen_eliminate(screen_accuracy):
    """先将以出现号码储存为列表，之后剔除"""
    def __init__(self):
        super(screen_eliminate,self).__init__()
        self.el_num = []

    def eliminate_num(self):
        """这个类记录每次随机的一个开奖号码"""
        self.el_num.append(self.onenum)
        #self.el_num.sort() #对剔除的列表排序，否则容易超出列表长度
        #self.el_num.reverse()#反序，先剔除大号码

    def tichu(self):
        if self.onenum not in self.el_num:
            self.thousand.remove(self.onenum)
        else:
            pass

if __name__ == "__main__":
    a = screen_eliminate()
    cs = 0
    a.newthousand()
    cs += 1
    a.onenumber()
    a.standard_random()
    a.obtain_all_yes_no()
    while cs < 1000:
        cs += 1
        a.onenumber()
        a.eliminate_num()
        a.standard_random()
        a.obtain_all_yes_no()
        a.tichu()
    print(a.el_num)
    print(len(a.random200s))
    print(len(a.thousand))
    print(a.thousand)
    a.calculate()
    a.all_print()
