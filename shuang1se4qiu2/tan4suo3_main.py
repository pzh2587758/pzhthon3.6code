from tan4suo3_号码储存方式 import ce4shi4 
from biao1_ti_main import Biao1_Ti2
from lu4_ru4 import Lu4_Ru4

zhubiaoti = Biao1_Ti2()
zhubiaoti.zhu3_jie4_mian4()

lu4_ru4 = Lu4_Ru4()
num = input("请输入选中的号码：")
if num == "1":
    test_dui4xiang4 = ce4shi4(lu4_ru4.xun2_wen4())
else:
    print("没有这个号码")

zhongjianghao_5 = ["1","2","3","4","8"]
zhongjianghao_2 = ["a","c"]

b = test_dui4xiang4.shu1ru4hao4ma3()
print('\33[1;31;40m')
print('返回的字典类型为：',str(b))
print("_______________分割线__________________________")
print('\33[0m')

print("分割红球和蓝球，分别组成数组")
print(test_dui4xiang4.jian3cha2_he2fa3_h5(b))
print(test_dui4xiang4.jian3cha2_he2fa3_l2(b))
print("_______________分割线__________________________")

#比较红球中奖个数
print("测试的中奖号码：" + str(zhongjianghao_5))
print("测试的中奖号码：" + str(zhongjianghao_2))

print("红球中了{}个".format(test_dui4xiang4.pan4_duan4(zhongjianghao_5,test_dui4xiang4.jian3cha2_he2fa3_h5(b))))
        
print("蓝球中了{}个".format(test_dui4xiang4.pan4_duan4(zhongjianghao_2,test_dui4xiang4.jian3cha2_he2fa3_l2(b))))
