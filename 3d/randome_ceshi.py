import random
import time

#200个猜测结果
def random200():
    thousand = list(range(1,1000)) #生成1-999的数列
    random200s = random.sample(thousand,200) #.sample抽取数列，这样不会出现重复数
    random200s.sort()
    print('200个猜测结果：' + str(random200s))
    return random200s

#100个待猜开奖号码
def random100zjh():
    th = list(range(1,1000))
    ran100zjh = random.sample(th,100)
    print('100个模拟开奖号码：' + str(ran100zjh))
    return ran100zjh

def bijiao(ran100zjh,random200s):
    ratrue = 0
    rafalse = 0
    for ran100 in ran100zjh:
        right =0
        error = 0
        for ran200 in random200s:
            #time.sleep(0.01)
            #print('开奖号码：{}猜测号码：{}'.format(ran100,ran200))
            if ran200 == ran100:
                ratrue += 1
                right += 1
                #print('猜对一个!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            else:
                rafalse += 1
                error += 1
        right_error = right/(right + error)
        print('正确：{}，错误：{}，正确率：{:.2%}'.format(right,error,right_error))
    raall = ratrue/(ratrue + rafalse)
    print('正确：{}，错误：{}，正确率：{:.2%}'.format(ratrue,rafalse,raall))
    
b = random200()
a = random100zjh()
bijiao(a,b)
