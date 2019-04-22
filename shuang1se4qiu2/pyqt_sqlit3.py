
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
from PyQt5.QtCore import Qt



def initializeModel(model):
    model.setTable('c')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)#OnFieldChange所有变更实时更新
    model.select()
    model.setHeaderData(0,Qt.Horizontal,"ID")
    
#    model.setTable('kai1_jiang3_hao4')
#    model.setEditStrategy(QSqlTableModel.OnFieldChange)
#    model.select()
#    model.setHeaderData(0,Qt.Horizontal,"ID")
#    model.setHeaderData(1,Qt.Horizontal,"LEI4_XING2 TEXT")
#    model.setHeaderData(2,Qt.Horizontal,"h1")
#    model.setHeaderData(3,Qt.Horizontal,"h2")
#    model.setHeaderData(4,Qt.Horizontal,"h3")
#    model.setHeaderData(5,Qt.Horizontal,"h4")
#    model.setHeaderData(6,Qt.Horizontal,"h5")
#    model.setHeaderData(7,Qt.Horizontal,"l1")
#    model.setHeaderData(8,Qt.Horizontal,"l2")

def createView(title,model):
    """创建一个QTableView窗口，用来容纳QSqlTablemodel的"""
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow():
    ret = model.insertRows(model.rowCount(),1)
    #print('insertRows={}'.format(str(ret)))
#    if ret == False:
#        QMessageBox.about(dlg,"错误","数据超出范围")

def findrow(i):
    delrow = i.row()
    print('del row ={}'.format(str(delrow)))



app = QApplication(sys.argv)
#创建app对象****************************

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName('num_sql.db')
#创建并打开一个到sqlite3的连接>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

model = QSqlTableModel()
delrow = -1
initializeModel(model)

view1 = createView("Table Model (View 1)",model)
view1.clicked.connect(findrow)


dlg = QDialog()
layout = QVBoxLayout()
layout.addWidget(view1)

addBtn = QPushButton("zen")
addBtn.clicked.connect(addrow)
layout.addWidget(addBtn)

delBtn = QPushButton("del") #这个删除有问题
index = view1.currentIndex()
print(index.row())
delBtn.clicked.connect(lambda:model.removeRow(index.row()))
#removeRow删除行,currentIndes().row()获取选中行
layout.addWidget(delBtn)

dlg.setLayout(layout)
dlg.setWindowTitle("database")
dlg.resize(1024,960)
dlg.show()

sys.exit(app.exec_())
#关闭app对象******************************


