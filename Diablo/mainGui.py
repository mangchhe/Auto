"""
    작성일 : 20/09/27
"""
import sys

from jewelry import jewelryCombineMain, jewelryCombineMain2, jewelryCombineMain3
from hotkey import hotkeyMain

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        hotkeyMain()

        self.initUI()

    def initUI(self):

        btn = QPushButton('보석 낱개 조합', self)
        btn.clicked.connect(jewelryCombineMain)
        btn2 = QPushButton('퍼보 만들어 보석 조합', self)
        btn2.clicked.connect(jewelryCombineMain2)
        btn3 = QPushButton('통합 조합', self)
        btn3.clicked.connect(jewelryCombineMain3)

        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        
        self.setLayout(vbox)
        self.setWindowTitle('디아블로 매크로')
        self.setWindowIcon(QIcon('diablo_favicon.ico'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
