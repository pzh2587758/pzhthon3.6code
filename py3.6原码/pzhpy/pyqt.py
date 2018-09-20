import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#import random_number_create


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(1200, 1000)
        self.setWindowTitle("潘震海的程序")
        self.initUI()

    def initUI(self):
        # 创建一个菜单栏
        bar = self.menuBar()
        file = bar.addMenu("file")
        file.addAction("new")

        label1 = QLabel('服务器图片')
        label2 = QLabel('断开/连接')

        button1 = QPushButton("连接")
        button2 = QPushButton("断开")
        button3 = QPushButton("增")
        button4 = QPushButton("删")
        button5 = QPushButton("查")
        button6 = QPushButton("改")
        button7 = QPushButton("爬取")
        button8 = QPushButton("查看csv")
        button9 = QPushButton("导入mysql")
        button10 = QPushButton("计算")
        button11 = QPushButton("预测")

        tableWidget1 = QTableWidget()
        tableWidget1.setRowCount(20)
        tableWidget1.setColumnCount(2)
        tableWidget1.setHorizontalHeaderLabels(['期号', '开奖号'])

        # 创建网格
        grid = QGridLayout()
        grid.setSpacing(8)

        # 控件在网格中的坐标
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 2)
        grid.addWidget(button1, 0, 1)
        grid.addWidget(button2, 0, 3)
        grid.addWidget(button3, 8, 0)
        grid.addWidget(button4, 8, 1)
        grid.addWidget(button5, 8, 2)
        grid.addWidget(button6, 8, 3)
        grid.addWidget(button7, 1, 3)
        grid.addWidget(button8, 1, 4)
        grid.addWidget(button9, 2, 3)
        grid.addWidget(button10, 2, 4)
        grid.addWidget(button11, 3, 3)
        grid.addWidget(tableWidget1, 1, 0, 6, 2)

        # 创建一个窗口
        main_frame = QWidget()
        # 设置窗口布局为grid
        main_frame.setLayout(grid)
        # 设置为主窗口的中心窗口
        self.setCentralWidget(main_frame)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
