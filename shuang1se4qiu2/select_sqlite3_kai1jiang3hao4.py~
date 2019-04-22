import sqlite3

class select_kai1_jiang3_hao4(object):
    """从数据库提取数据，生成开奖号的字典"""
    def __init__(self):
        self.use_table = "kai1_jiang3_num" #表名
        self.use_database = "num_sql.db" #数据库名
        self.rows_l2 = "l1,l2"
        self.rows_h5 = "h1,h2,h3,h4,h5" #需要查找的列名
        self.where = "where qi1_hao4 = 2019042" #需要查找的行的where设置
        self.columns = []
        self.conn = None
        self.c = None

    def open_sqlite3_num_sql_db(self):
        """1.打开数据库"""
        self.conn = sqlite3.connect(self.use_database)
        self.c = self.conn.cursor()
        print("成功打开数据库{}".format(self.use_database))
        print("读取{}".format(self.use_table))

    def execute_num_sql_db_h5(self):
        """2.执行execute"""
        cursor = self.c.execute(
                "select {} from {} {} ;".format(self.rows_h5,self.use_table,self.where))
        self.columns = cursor.fetchall()
        #a = cursor.fetchone()

    def execute_num_sql_db_l2(self):
        """3.关闭数据库"""
        cursor = self.c.execute(
                "select {} from {} {} ;".format(self.rows_l2,self.use_table,self.where))
        self.columns = cursor.fetchall()


    def close_num_sql_db(self):
        print("关闭{}".format(self.use_table))
        self.conn.close()

    def chai1_bao1(self):
        """对查找到的数据进行拆包"""
        kai1_jiang3_tuple = self.columns[0]
        return kai1_jiang3_tuple

class select_test_num(select_kai1_jiang3_hao4):
    def __init__(self):
        super().__init__()
        self.use_table = "test_num"


class dui4_bi3():
    """对比两组号码，成功了,但太蠢了"""
    def __init__(self,kai1jiang3hao4,dui4bi3hao4):
        self.kai1jiang3hao4 = kai1jiang3hao4
        self.dui4bi3hao4 = dui4bi3hao4

    def test_duibi(self):
        print("开奖号为：")
        print(self.kai1jiang3hao4)
        for i in self.dui4bi3hao4:
            z = 0
            print("数组元组拆出的元组为：" + str(i))
            for j in self.kai1jiang3hao4:
                #print("开奖号码单独出来一个：" + str(j))
                for x in i:
                    if x == j:
                        z += 1
                    #print("元组单独出来的一个为：" + str(x))
            print("z = " + str(z))


if __name__ == "__main__":
    a_kaijiang = select_kai1_jiang3_hao4()
    a_kaijiang.open_sqlite3_num_sql_db()
    a_kaijiang.execute_num_sql_db_h5()
    a_kaijiang.close_num_sql_db()
    b_5 = a_kaijiang.chai1_bao1()

    a_kaijiang = select_kai1_jiang3_hao4()
    a_kaijiang.open_sqlite3_num_sql_db()
    a_kaijiang.execute_num_sql_db_l2()
    a_kaijiang.close_num_sql_db()
    b_2 = a_kaijiang.chai1_bao1()
    
    c_caice = select_test_num()
    c_caice.open_sqlite3_num_sql_db()
    c_caice.execute_num_sql_db_h5()
    c_caice.close_num_sql_db()
    d_5 = c_caice.columns

    c_caice = select_test_num()
    c_caice.open_sqlite3_num_sql_db()
    c_caice.execute_num_sql_db_l2()
    c_caice.close_num_sql_db()
    d_2 = c_caice.columns

    duibi = dui4_bi3(b_5,d_5)
    duibi.test_duibi()

    duibi = dui4_bi3(b_2,d_2)
    duibi.test_duibi()
