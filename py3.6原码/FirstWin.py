import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget

class WinForm(QWidget):
    def __init__(self, parent =None):
        super(WinForm, self).__init__(parent)#创建一个重写的窗口类
        self.setGeometry(300, 300, 350, 350)#窗口大小
        self.setWindowTitle('点击按钮关闭窗口')#窗口标题
        quit = QPushButton('Close', self)#创建一个button按钮
        quit.setGeometry(10, 10, 60, 35)#按钮位置
        quit.setStyleSheet("background-color:blue")#按钮背景色
        quit.clicked.connect(self.close)#按钮点击事件
        
if __name__=="__main__":
    app = QApplication(sys.argv)#APP开始
    win = WinForm()#创建一个WINFORM对象
    win.show()#显示这个对象
    sys.exit(app.exec_())#APP结束
        
