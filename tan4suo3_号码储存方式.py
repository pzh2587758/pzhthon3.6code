class ce4shi4():
    
    def shu1ru4hao4ma3(self):
        """将录入的字符串格式的猜测号码，转换为常规的字典类型"""
        print('\033[1;31;40m') #终端颜色
        print("彩票格式5+2")
        jie1shou4_string = input("请输入号码，按照'期号，分类，红1...蓝2'的格式:\n")
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

    def jian3cha2_he2fa3(self,jian3cha2_jie1shou4_num):
        """将合法获得的字典类型中的红球和蓝球的号码提取出来，成为一个数组"""
        da4le4tou4_5_2 = [
            jian3cha2_jie1shou4_num["h1"],
            jian3cha2_jie1shou4_num["h2"],
            jian3cha2_jie1shou4_num["h3"],
            jian3cha2_jie1shou4_num["h4"],
            jian3cha2_jie1shou4_num["h5"],
            jian3cha2_jie1shou4_num["l1"],
            jian3cha2_jie1shou4_num["l2"]
        ]
        return da4le4tou4_5_2
        
    def ce4shi4_1(self):
        """测试常规字典储存期号，分类，红1等信息"""
        kai1jiang3_num = {"qi1hao4":"201903028","fen1lei4":"kai1jiang3hao4","h1":1,"h2":2,"h3":3,"h4":4,"l1":5,"l2":6}
        a = kai1jiang3_num["qi1hao4"]
        if a == "201903028":
            print(kai1jiang3_num["qi1hao4"])
        else:
            print("error")



a = ce4shi4()
#a.ce4shi4_1()
b = a.shu1ru4hao4ma3()
print('返回的字典类型为：',str(b))
print(a.jian3cha2_he2fa3(b))

