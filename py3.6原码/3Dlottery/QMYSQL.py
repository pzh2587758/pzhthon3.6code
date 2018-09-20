from PyQt5.QtSql import QSqlDatabase

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost:3306")
db.setDatabaseName("pzh")
db.setUserName("root")
db.setPassword("pzh.2587758.hehe")
query = db.open()
query.exec_("use pzh")
query.exec("show tables;")
db.close()
