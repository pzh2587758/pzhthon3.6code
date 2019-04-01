class ce4shi4():
    def __init__(self,test):
        self.test_num = test
    
    def shu1ru4hao4ma3(self):
        """将录入的字符串格式的猜测号码，转换为常规的字典类型"""
        print('\033[1;31;40m') #终端颜色
        print('*'*50)
        print("彩票格式5+2")
        jie1shou4_string = self.test_num #input("请输入号码，按照'期号，分类，红1...蓝2'的格式:\n")
        cai1ce4_num = jie1shou4_string.split(',') #split,rsplit
        jie1shou4_num = {"qi1hao4":"","fen1lei4":"","h1":None,"h2":None,"h3":None,"h4":None,"h5":None,"l1":None,"l2":None}
        a = 0 #遍历计数器
        for name in jie1shou4_num.keys(): #keys()
            """遍历5+2字典，将录入数组的列表逐个赋值给字典的键。"""
            try:
                jie1shou4_num[name] = cai1ce4_num[a]
            except :
                print('\033[1;35;43m')
                print("格式错误，请检查录入的数据格式。")
                break
            a += 1
        print('\033[1;36;40m')
        print('录入的字符串转换为列表后为：' + str(cai1ce4_num))
        print('生成的字典为：')
        print(jie1shou4_num)
        print('\033[0m')
        return jie1shou4_num

    def jian3cha2_he2fa3_h5(self,jian3cha2_jie1shou4_num):
        """将合法获得的字典类型中的红球的号码提取出来，成为一个数组"""
        da4le4tou4_5 = [
            jian3cha2_jie1shou4_num["h1"],
            jian3cha2_jie1shou4_num["h2"],
            jian3cha2_jie1shou4_num["h3"],
            jian3cha2_jie1shou4_num["h4"],
            jian3cha2_jie1shou4_num["h5"]
        ]
        return da4le4tou4_5

    def jian3cha2_he2fa3_l2(self,jian3cha2_jie1shou4_num):
        """将合法获得的字典类型中的蓝球的号码提取出来，成为一个数组"""
        da4le4tou4_2 = [
                jian3cha2_jie1shou4_num["l1"],
                jian3cha2_jie1shou4_num["l2"]
                ]
        return da4le4tou4_2

    
    def pan4_duan4(self,p1_5,p2_5):
        """检测红球五个球是否中奖"""
        a = 0
        for i in p1_5:
            for j in p2_5:
                if i == j:
                    print("中")
                    a += 1
        return a
        



