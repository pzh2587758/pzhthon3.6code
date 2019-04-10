
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
from PyQt5.QtCore import Qt

def initializeModel(model):
    model.setTable('kai1_jiang3_hao4')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0,Qt.Horizontal,"ID")
    model.setHeaderData(1,Qt.Horizontal,"LEI4_XING2 TEXT")
    model.setHeaderData(2,Qt.Horizontal,"h1")
    model.setHeaderData(3,Qt.Horizontal,"h2")
    model.setHeaderData(4,Qt.Horizontal,"h3")
    model.setHeaderData(5,Qt.Horizontal,"h4")
    model.setHeaderData(6,Qt.Horizontal,"h5")
    model.setHeaderData(7,Qt.Horizontal,"l1")
    model.setHeaderData(8,Qt.Horizontal,"l2")

def createView(title,model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow():
    ret = model.insertRows(model.rowCount(),1)
    print('insertRows={}'.format(str(ret)))

def findrow(i):
    delrow = i.row()
    print('del row ={}'.format(str(delrow)))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName('num_sql.db')
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

    delBtn = QPushButton("del")
    delBtn.clicked.connect(lambda:
            model.removeRow(view1.currentIndex().row()))
    layout.addWidget(delBtn)
    dlg.setLayout(layout)
    dlg.setWindowTitle("database")
    dlg.resize(1024,960)
    dlg.show()
    sys.exit(app.exec_())



