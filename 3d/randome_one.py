#python3.6
#关于每期200次随机猜测的正确率
import random

class screen_accuracy():
    """这是3D随机200个数猜测的正确率计算类"""
    def __init__(self):
        self.cs = 0
        self.cz = 0
        self.wcz = 0
        self.right = 0
        self.raall = 0
        self.lirun = 0
        self.onenum = 0
        self.random200s = [] 
        self.thousand = []

    #输出一个标准三位数,用于作为随机开奖号码
    def onenumber(self):
        self.onenum  = random.randint(1, 1000)

    #传递猜测号码给算法    
    def standard_random(self):
        self.random200s = random.sample(self.thousand, 200)
        self.random200s.sort()

    def newthousand(self):
        newthousand = list(range(1, 1000))
        self.thousand = newthousand
        


    #总次数，猜中次数，未猜中次数
    def obtain_all_yes_no(self):
        for ran200 in self.random200s:
            if ran200 == self.onenum:
                self.right = True
                break
            else:
                self.right = False
        self.cs += 1
        if self.right == True:
            self.cz += 1
            
    def calculate(self):
        self.wcz = self.cs - self.cz
        self.raall = self.cz/self.cs
        self.lirun = self.cz*1000 - self.cs*400
        
    def all_print(self):
        print('进行了{}期猜测，猜中：{},未猜中：{},正确率：{:.2%}'.format(self.cs, self.cz, self.wcz, self.raall))
        print('每100期利润为：' + str(self.lirun))
        
if __name__ == "__main__":
    def onetrue():
        a = screen_accuracy()
        cs =0
        a.newthousand()
        while cs <1000:
            cs += 1
            a.onenumber()
            a.standard_random()
            a.obtain_all_yes_no()
        a.calculate()
        a.all_print()
    onetrue()
