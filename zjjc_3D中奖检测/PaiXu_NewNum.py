
class zjjc(object):
    """规范号码用"""
    def __init__(self): 
        pass

    def paixu_NewNum(self,old_num):
        """正向排序号码"""
        num_num = []
        for n in old_num[3:]:
            num_num.append(int(n))
        print("3:")
        print(num_num)
        list0_3 = old_num[:3]
        old_num = list0_3 + num_num
        print(old_num)
        zjh_7 = old_num[3:8]
        zjh_7.sort()
        zjh_2 = old_num[8:]
        zjh_2.sort()
        zjh_7.extend(zjh_2)
        zjh_new = old_num[0:3]
        zjh_new.extend(zjh_7)
        return zjh_new
