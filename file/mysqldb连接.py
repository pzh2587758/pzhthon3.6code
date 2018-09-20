#python3

import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='pzh.2587758.hehe',db='pzh',port=3306,charset='utf8')

cur = db.cursor()  #游标

cur.execute('SELECT VERSION()')

data = cur.fetchone()  #获取单条数据

print('数据库版本: %s' % data)

sql = """CREATE TABLE employee(first_name CHAR(20) NOT NULL,last_name CHAR(20),
age int(10),sex CHAR(5),income FLOAT)"""

cur.execute(sql)

cur.close()
db.close()
