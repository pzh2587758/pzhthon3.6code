#! python3 utf-8

class Lu4_Ru4():
    """这个类用来将开奖号码和购买的号码进行保存"""
    
    def xun2_wen4(self):
        """询问"""
        xuan3_ze2 = input("输入1录入中奖号码，输入2录入购买的号码")
        if xuan3_ze2 == "1":
            kai1_jiang3_num = input("请按照格式输入开奖号，用逗号分开")
            test_num = "2019,hehe,1,2,3,4,5,a,b"
            return test_num
        elif xuan3_ze2 == "2":
            gou4_mai3_num =  input("请输入购买的号码：")
            print(gou4_mai3_num)
            return gou4_mai3_num

            
if __name__ == "__main__":
    a = Lu4_Ru4()
    gou4_mai3_num = a.xun2_wen4()
    print(str(gou4_mai3_num))
