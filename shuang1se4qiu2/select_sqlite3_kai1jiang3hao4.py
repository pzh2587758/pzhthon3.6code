import sqlite3

class select_kai1_jiang3_hao4():
    """从数据库提取数据，生成开奖号的字典"""

    def select_kai1_jiang3(self):
        conn = sqlite3.connect('num_sql.db')
        c = conn.cursor()
        print("成功打开数据库")
        print("读取数据库")

        cursor = c.execute("select * from kai1_jiang3_hao4;")
        a = cursor.fetchall()
        print("关闭数据库")
        conn.close()
        print("返回的开奖号码为：")
        return a
#       return ur

if __name__ == "__main__":
    a = select_kai1_jiang3_hao4()
    b = a.select_kai1_jiang3()
    print(b)
    print(len(b))
    lists = {}
    for i in range(len(b)):
        lists[i] = b[i]
    print(lists)
    print(lists[0][0])
    print(lists[1][0])
    print(lists[2][0])
        
    kaijianghao = {"ri4_qi":"","lei_xing":"","h1":"","h2":"","h3":"","h4":"","h5":"","l1":"","l2":""}

