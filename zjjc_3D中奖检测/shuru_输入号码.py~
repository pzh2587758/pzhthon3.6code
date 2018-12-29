from PaiXu_NewNum import zjjc

class shuru_num(object):
    def __init__(self):
        self.Tou = """
        ************************
        *请输入序列号进行操作  *
        *----------------------*
        *1,输入开奖号码        *
        *2,没想好              *
        ************************
        """ 

    def shuru(self):
        while True:
            print(self.Tou)
            tou_one = input("主页面数字选择：")
            if tou_one == "1":
                print("格式为开奖号，日期，期号，第一位数...类推。")
                #tou1_1 = input("请输入，用逗号隔开:")
                tou1_1 = "开奖号,2018-12-29,18xxx,12,8,24,30,31,10,5"
                x = tou1_1.split(",")
                print(x)
                a = zjjc()
                print(a.paixu_NewNum(x))
            elif tou_one == "2":
                print("2")
            elif tou_one == "3":
                print("3")
            elif tou_one == "Q":
                break
            else:
                print("数字不存在")

b = shuru_num()
b.shuru()
