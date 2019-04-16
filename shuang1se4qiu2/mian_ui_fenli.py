import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from mian_ui import *

class main_window(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(main_window,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = main_window()
    mainwin .show()
    sys.exit(app.exec_())
