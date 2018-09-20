# UTF8

import pymysql

conn=pymysql.connect(host='localhost',user='root',passwd='pzh.2587758.hehe',db='pzh',port=3306,charset='utf8')

cur=conn.cursor()             #获取一个游标

sql ="SELECT * FROM 3dnum; # WHERE lottery_number='339';"   #mysql语句

cur.execute(sql)              #执行语句

results = cur.fetchall()      #获取记录列表



for row in results:           #逐行打印
    id = row[0]
    issub = row[1]
    num = row[2]
    print('ID：%s,期号：%s,开奖号码：%s'%(id,issub,num))


cur.close()#关闭游标
conn.close()#释放数据库资源
