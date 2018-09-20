import random

class ran1000():
    def __init__(self):
        
        """生成一个1——1000的数字列表，从中随机抽取200个"""


        """生成200个随机数并排序，打印出来"""
        
        self.thousand = list(range(1,1000))
        self.random200s = random.sample(thousand,200)
        self.random200s.sort()
        return self.random200s

##        """开奖号码"""
##        ceshi = 529
##        print("当期开奖号码为" + str(ceshi))
##
##        """判断开奖号码是否在随机数中，并确定a的值"""
##        for random200 in random200s:
##            if random200 == ceshi:
##                 a = True
##                 break
##            else:
##                 a = False
##
##        """根据a的值输出"""
##        if(a==True):
##             print("恭喜你中奖了")
##        else:
##             print("没中")

if __name__ == "__main__":
    a = ran1000()
    print(a)
    
