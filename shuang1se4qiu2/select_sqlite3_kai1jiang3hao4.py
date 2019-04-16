import sqlite3

class select_kai1_jiang3_hao4():
    """从数据库提取数据，生成开奖号的字典"""

    def select_kai1_jiang3(self):
        conn = sqlite3.connect('num_sql.db')
        c = conn.cursor()
        print("成功打开数据库")
        print("读取数据库")

        cursor = c.execute("select * from d;")
        a = cursor.fetchall()
        print("关闭数据库")
        conn.close()
        return a

if __name__ == "__main__":
    a = select_kai1_jiang3_hao4()
    b = a.select_kai1_jiang3()
    print("返回的开奖号码为：")
    print(b)
    print("列表长度为：")
    print(len(b))
    lists = {}
    for i in range(len(b)):
        lists[i] = b[i]
    for key,value in lists.items():
        print(str(key) + ":" + str(value))
        
        
    kaijianghao = {"ri4_qi":"","lei_xing":"","h1":"","h2":"","h3":"","h4":"","h5":"","l1":"","l2":""}

