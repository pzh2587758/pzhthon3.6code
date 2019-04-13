import sqlite3

"""
1.这个程序用来论证，当sqlite3中的数值约束错误时，python3是怎么报错的
2.批量对数据库插入时，批量报错的演示
"""

conn = sqlite3.connect('num_sql.db')
c = conn.cursor()
print("successfully")

lister = [
        "INSERT INTO c (id) VALUES (6)",
        "INSERT INTO c (id) VALUES (5)",
        "INSERT INTO c (id) VALUES (7)",
        "INSERT INTO c (id) VALUES (8)",
        "INSERT INTO c (id) VALUES (9)"
        ]
        
for i in lister:
    try:
        c.execute(i);
    except sqlite3.IntegrityError:
        print("{}插入的数据不在取值范围内".format(i))
    else:
        print("{}插入成功".format(i))
conn.commit()
print("succesfully")
conn.close()
