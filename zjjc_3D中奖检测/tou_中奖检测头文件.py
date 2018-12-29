#!python3.6
from PaiXu_NewNum import zjjc
#from shuru_输入号码 import shuru_num

"""
目前完成了规范号码类
存储号码
比较号码
得分规则
记分
"""

cszj_测试中奖号 = ["开奖号","2018-12-10",18145,18,9,29,31,33,11,6]
cscp_测试出票号 = ["出票号","2018-12-10",18145,17,4,12,31,33,2,11]

#b = shuru_num()
#b.shuru()

a = zjjc()
print(a.paixu_NewNum(cszj_测试中奖号))
print(a.paixu_NewNum(cscp_测试出票号))

