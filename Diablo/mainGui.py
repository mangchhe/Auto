"""
    작성일 : 20/09/27
"""
import sys

from jewelry import Jewelry
from hotkey import hotkeyMain
from room import Room

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        
        hotkeyMain()
        self.room = Room()
        self.jewelry = Jewelry()
        self.initUI()

    def initUI(self):

        btn = QPushButton('보석 낱개 조합(F2)')
        btn.clicked.connect(self.jewelry.jewelryCombineMain2)
        btn2 = QPushButton('퍼보 만들어 보석 조합(F3)')
        btn2.clicked.connect(self.jewelry.jewelryCombineMain)
        btn3 = QPushButton('통합 조합(F4)')
        btn3.clicked.connect(self.jewelry.jewelryCombineMain3)
        btn4 = QPushButton('방 리셋(F5)')
        btn4.clicked.connect(self.room.main)
        btn5 = QPushButton('종료')
        btn5.clicked.connect(QCoreApplication.instance().quit)

        leftBox1 = QGroupBox('기능')

        leftTop = QVBoxLayout()
        leftTop.addWidget(btn)
        leftTop.addWidget(btn2)
        leftTop.addWidget(btn3)
        leftTop.addWidget(btn4)
        leftTop.addWidget(btn5)

        leftBox = QVBoxLayout()
        leftBox.addLayout(leftTop)

        leftBox1.setLayout(leftBox)

        rightBox1 = QGroupBox('D2Loader')
        self.rightRadio1 = QRadioButton('노말')
        self.rightRadio1.setChecked(True)
        self.rightRadio1.clicked.connect(self.RadioButtonClicked)
        self.rightRadio11 = QRadioButton('나이트메어')
        self.rightRadio11.clicked.connect(self.RadioButtonClicked)
        self.rightRadio111 = QRadioButton('헬')
        self.rightRadio111.clicked.connect(self.RadioButtonClicked)
        
        rightBox2 = QGroupBox('D2Loader2')
        self.rightRadio2 = QRadioButton('노말')
        self.rightRadio2.setChecked(True)
        self.rightRadio2.clicked.connect(self.RadioButtonClicked2)
        self.rightRadio22 = QRadioButton('나이트메어')
        self.rightRadio22.clicked.connect(self.RadioButtonClicked2)
        self.rightRadio222 = QRadioButton('헬')
        self.rightRadio222.clicked.connect(self.RadioButtonClicked2)

        rightBox3 = QGroupBox('D2Loader3')
        self.rightRadio3 = QRadioButton('노말')
        self.rightRadio3.setChecked(True)
        self.rightRadio3.clicked.connect(self.RadioButtonClicked3)
        self.rightRadio33 = QRadioButton('나이트메어')
        self.rightRadio33.clicked.connect(self.RadioButtonClicked3)
        self.rightRadio333 = QRadioButton('헬')
        self.rightRadio333.clicked.connect(self.RadioButtonClicked3)

        right1 = QHBoxLayout()
        right1.addWidget(self.rightRadio1)
        right1.addWidget(self.rightRadio11)
        right1.addWidget(self.rightRadio111)
        rightBox1.setLayout(right1)

        right2 = QHBoxLayout()
        right2.addWidget(self.rightRadio2)
        right2.addWidget(self.rightRadio22)
        right2.addWidget(self.rightRadio222)
        rightBox2.setLayout(right2)

        right3 = QHBoxLayout()
        right3.addWidget(self.rightRadio3)
        right3.addWidget(self.rightRadio33)
        right3.addWidget(self.rightRadio333)
        rightBox3.setLayout(right3)

        rightGbox = QGroupBox('방 리셋 환경설정')
        roomVbox = QVBoxLayout()
        roomVbox.addWidget(rightBox1)
        roomVbox.addWidget(rightBox2)
        roomVbox.addWidget(rightBox3)
        rightGbox.setLayout(roomVbox)

        layout = QGridLayout()

        layout.addWidget(leftBox1, 0, 0)
        layout.addWidget(rightGbox, 0, 1)
        
        self.setLayout(layout)
        self.setWindowTitle('디아블로 매크로')
        self.setWindowIcon(QIcon('diablo_favicon.ico'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def RadioButtonClicked(self):
        if self.rightRadio1.isChecked():
            self.room.setDifficulty(1)
        elif self.rightRadio11.isChecked():
            self.room.setDifficulty(2)
        elif self.rightRadio111.isChecked():
            self.room.setDifficulty(3)

    def RadioButtonClicked2(self):
        if self.rightRadio2.isChecked():
            self.room.setDifficulty2(1)
        elif self.rightRadio22.isChecked():
            self.room.setDifficulty2(2)
        elif self.rightRadio222.isChecked():
            self.room.setDifficulty2(3)

    def RadioButtonClicked3(self):
        if self.rightRadio3.isChecked():
            self.room.setDifficulty3(1)
        elif self.rightRadio33.isChecked():
            self.room.setDifficulty3(2)
        elif self.rightRadio333.isChecked():
            self.room.setDifficulty3(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
