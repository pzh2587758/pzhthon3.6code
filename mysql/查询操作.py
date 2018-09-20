import pymysql


class pymysql_select():

    def connect_open(self):
        db = pymysql.connect(host="localhost",user="root",password="pzh.2587758.hehe",
                db="pzh")
        cursor =db.cursor()
        cursor.execute("select * from 3d")
        results = cursor.fetchall()
        filename = '3d.py'
        with open(filename,'w') as file_object:
            for row in results:
                id = str(row[0])
                issue = str(row[1])
                file_object.write("{} {}\n".format(id,issue))
        cursor.close()
        db.close()

a = pymysql_select()
a.connect_open()
