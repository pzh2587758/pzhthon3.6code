import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","pzh.2587758.hehe","pzh" )
 
# 使用 cursor() 方法创建一个游标对象 cursor,就是获取操作游标
cursor = db.cursor()
#————————————————————————————————


 
# 使用 execute()  方法执行 SQL 语句 
data1 = cursor.execute("show databases")
print(data1)
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)

#获取最新自增id
new_id = cursor.lastrowid
print(new_id)

#获取表的行数
print(data1)



#——————————————————————————————————
#关闭操作游标
cursor.close()
#关闭数据库
db.close()
