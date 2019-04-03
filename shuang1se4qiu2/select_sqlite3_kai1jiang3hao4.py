import sqlite3

class select_kai1_jiang3_hao4():
    """从数据库提取数据，生成开奖号的字典"""

    def select_kai1_jiang3(self):
        conn = sqlite3.connect('num_sql.db')
        c = conn.cursor()
        print("成功打开数据库")

        cursor = c.execute("select * from kai1_jiang3_hao4;")
        kaijianghao = {"ri4_qi":"","lei_xing":"","h1":"","h2":"","h3":"","h4":"","h5":"","l1":"","l2":""}
        for row in cursor:
            kaijianghao["ri4_qi"] = row[0]
            kaijianghao["lei_xing"] = row[1]
            kaijianghao["h1"] = row[2]
            kaijianghao["h2"] = row[3]
            kaijianghao["h3"] = row[4]
            kaijianghao["h4"] = row[5]
            kaijianghao["h5"] = row[6]
            kaijianghao["l1"] = row[7]
            kaijianghao["l2"] = row[8]
            print(kaijianghao)
        print("关闭数据库")
        conn.close()

a = select_kai1_jiang3_hao4()
a.select_kai1_jiang3()

