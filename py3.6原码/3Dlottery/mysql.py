#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "pzh.2587758.hehe", "pzh")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# SQL 查询语句
sql = "SELECT * FROM 3D0 "

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        ID = row[0]
        KAIJIANGHAOMA = row[1]

        # 打印结果
        print("ID=%s,KAIJIANGHAOMA=%s" %
              (ID, KAIJIANGHAOMA))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
