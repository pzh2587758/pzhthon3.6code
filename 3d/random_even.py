import random
from  randome_one import screen_accuracy

class even_accuracy(screen_accuracy):
    """这是3d随机200个偶数的正确率计算类"""
    def __init__(self):
        super(even_accuracy,self).__init__()
        

    #传递200个偶数进行猜测
    def standard_random(self):
        thousand = list(range(2,1000,2))
        self.random200s = random.sample(thousand,200)
        self.random200s.sort()

if __name__ == "__main__":
    a = even_accuracy()
    cs = 0
    while cs < 100:
        cs += 1
        a.onenumber()
        a.standard_random()
        a.obtain_all_yes_no()
    a.calculate()
    a.all_print()
