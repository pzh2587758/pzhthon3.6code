import sqlite3

class select_kai1_jiang3_hao4(object):
    """从数据库提取数据，生成开奖号的字典"""
    def __init__(self):
        self.use_table = "kai1_jiang3_num"
        self.use_database = "num_sql.db"
        self.rows = "*"
        self.where = "where qi1_hao4 = 2019042"

    def select_kai1_jiang3(self):
        conn = sqlite3.connect(self.use_database)
        c = conn.cursor()
        print("成功打开数据库{}".format(self.use_database))
        print("读取{}".format(self.use_table))

        cursor = c.execute("select {} from {} {} ;".format(self.rows,self.use_table,self.where))
        #a = cursor.fetchall()
        a = cursor.fetchone()
        print("关闭{}".format(self.use_table))
        conn.close()
        return a

class select_test_num(select_kai1_jiang3_hao4):
    def __init__(self):
        super().__init__()
        self.use_table = "test_num"
        self.rows = "qi1_hao4,yong4_tu2,h1,h2,h3,h4,h5,l1,l2"



if __name__ == "__main__":
    a = select_kai1_jiang3_hao4()
    b = a.select_kai1_jiang3()
    c = select_test_num()
    d = c.select_kai1_jiang3()
    print("返回的开奖号码为：")
    print(b)
    print("测试的猜测号码为：")
    print(d)
#    lists = {}
#    for i in range(len(b)):
#        lists[i] = b[i]
#    for key,value in lists.items():
#        print(str(key) + ":" + str(value))
        
        

