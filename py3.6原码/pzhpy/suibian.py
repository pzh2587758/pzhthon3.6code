import sys
from PyQt5.QtWidgets import *
from uixuexi import timeings


class pzhhehe(QWidget):

    def __init__(self, parent=None):
        super(pzhhehe, self).__init__(parent)
        self.setWindowTitle("pzhhehe")
        self.resize(300, 270)
        self.text = QTextEdit()
        self.but1 = QPushButton("timeing")
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.but1)
        self.setLayout(layout)

        self.but1.clicked.connect(self.but1_Clicked)

    def but1_Clicked(self):
        self.text.setPlainText()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pzhhehe()
    window.show()
    sys.exit(app.exec_())
