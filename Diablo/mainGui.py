"""
    작성일 : 20/09/27
"""
import sys

from jewelry import jewelryCombineMain, jewelryCombineMain2, jewelryCombineMain3
from hotkey import hotkeyMain
from room import Room

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        
        hotkeyMain()
        self.room = Room()
        self.initUI()

    def initUI(self):

        label = QLabel('Hello World!')
        label.setAlignment(Qt.AlignCenter)

        btn = QPushButton('보석 낱개 조합(F2)', self)
        btn.clicked.connect(jewelryCombineMain)
        btn2 = QPushButton('퍼보 만들어 보석 조합(F3)', self)
        btn2.clicked.connect(jewelryCombineMain2)
        btn3 = QPushButton('통합 조합(F4)', self)
        btn3.clicked.connect(jewelryCombineMain3)
        btn4 = QPushButton('방 리셋', self)
        btn4.clicked.connect(self.room.main)
        btn5 = QPushButton('종료', self)
        btn5.clicked.connect(QCoreApplication.instance().quit)

        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(btn5)

        layout = QVBoxLayout()
        layout.addLayout(vbox)
        layout.addLayout(hbox)
        
        self.setLayout(layout)
        self.setWindowTitle('디아블로 매크로')
        self.setWindowIcon(QIcon('diablo_favicon.ico'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
