"""
    작성일 : 20/09/27
"""
import sys

from jewelry import Jewelry
from hotkey import Hotkey
from room import Room

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QSize, QRect

class MyApp(QWidget):

    def __init__(self):

        super().__init__()

        self.room = Room()
        self.jewelry = Jewelry()
        hotkey = Hotkey(self.jewelry, self.room)
        hotkey.hotkeyMain()
        
        self.initUI()

    def initUI(self):

        btn = QPushButton('보석 낱개 조합(F9)')
        btn.clicked.connect(self.jewelry.jewelryCombineMain2)
        btn2 = QPushButton('퍼보 만들어 보석 조합')
        btn2.clicked.connect(self.jewelry.jewelryCombineMain)
        btn3 = QPushButton('통합 조합')
        btn3.clicked.connect(self.jewelry.jewelryCombineMain3)
        btn4 = QPushButton('방 리셋(F10)')
        btn4.clicked.connect(self.room.TogetherMain)
        btn5 = QPushButton('개별 방 리셋(F11)')
        btn5.clicked.connect(self.room.EachMain)
        btn6 = QPushButton('종료')
        btn6.clicked.connect(QCoreApplication.instance().quit)

        leftBox1 = QGroupBox('기능')

        leftTop = QVBoxLayout()
        leftTop.addWidget(btn)
        leftTop.addWidget(btn2)
        leftTop.addWidget(btn3)
        leftTop.addWidget(btn4)
        leftTop.addWidget(btn5)
        leftTop.addWidget(btn6)

        leftBox = QVBoxLayout()
        leftBox.addLayout(leftTop)
        leftBox1.setLayout(leftBox)

        centerBox1 = QGroupBox('텍스트, 앱 크기 비율')
        self.centerRadio1 = QRadioButton('100%')
        self.centerRadio1.setChecked(True)
        self.centerRadio1.clicked.connect(self.CenterRadioButtonClicked)
        self.centerRadio11 = QRadioButton('125%')
        self.centerRadio11.clicked.connect(self.CenterRadioButtonClicked)
        self.centerRadio111 = QRadioButton('150%')
        self.centerRadio111.clicked.connect(self.CenterRadioButtonClicked)

        center1 = QHBoxLayout()
        center1.addWidget(self.centerRadio1)
        center1.addWidget(self.centerRadio11)
        center1.addWidget(self.centerRadio111)
        centerBox1.setLayout(center1)

        centerGbox = QGroupBox('컴퓨터 환경설정')
        computerVbox = QVBoxLayout()
        computerVbox.addWidget(centerBox1)
        centerGbox.setLayout(computerVbox)

        self.rightBox1 = QGroupBox('D2Loader')
        self.rightBox1.setCheckable(True)
        self.rightBox1.setChecked(False)
        self.rightBox1.clicked.connect(self.RightBoxClicked)
        self.rightRadio1 = QRadioButton('노말')
        self.rightRadio1.setChecked(True)
        self.rightRadio1.clicked.connect(self.RightRadioButtonClicked)
        self.rightRadio11 = QRadioButton('나이트메어')
        self.rightRadio11.clicked.connect(self.RightRadioButtonClicked)
        self.rightRadio111 = QRadioButton('헬')
        self.rightRadio111.clicked.connect(self.RightRadioButtonClicked)
        
        self.rightBox2 = QGroupBox('D2Loader2')
        self.rightBox2.setCheckable(True)
        self.rightBox2.setChecked(False)
        self.rightBox2.clicked.connect(self.RightBoxClicked)
        self.rightRadio2 = QRadioButton('노말')
        self.rightRadio2.setChecked(True)
        self.rightRadio2.clicked.connect(self.RightRadioButtonClicked2)
        self.rightRadio22 = QRadioButton('나이트메어')
        self.rightRadio22.clicked.connect(self.RightRadioButtonClicked2)
        self.rightRadio222 = QRadioButton('헬')
        self.rightRadio222.clicked.connect(self.RightRadioButtonClicked2)

        self.rightBox3 = QGroupBox('D2Loader3')
        self.rightBox3.setCheckable(True)
        self.rightBox3.setChecked(False)
        self.rightBox3.clicked.connect(self.RightBoxClicked)
        self.rightRadio3 = QRadioButton('노말')
        self.rightRadio3.setChecked(True)
        self.rightRadio3.clicked.connect(self.RightRadioButtonClicked3)
        self.rightRadio33 = QRadioButton('나이트메어')
        self.rightRadio33.clicked.connect(self.RightRadioButtonClicked3)
        self.rightRadio333 = QRadioButton('헬')
        self.rightRadio333.clicked.connect(self.RightRadioButtonClicked3)

        right1 = QHBoxLayout()
        right1.addWidget(self.rightRadio1)
        right1.addWidget(self.rightRadio11)
        right1.addWidget(self.rightRadio111)
        self.rightBox1.setLayout(right1)

        right2 = QHBoxLayout()
        right2.addWidget(self.rightRadio2)
        right2.addWidget(self.rightRadio22)
        right2.addWidget(self.rightRadio222)
        self.rightBox2.setLayout(right2)

        right3 = QHBoxLayout()
        right3.addWidget(self.rightRadio3)
        right3.addWidget(self.rightRadio33)
        right3.addWidget(self.rightRadio333)
        self.rightBox3.setLayout(right3)

        rightGbox = QGroupBox('개별방 리셋 환경설정')
        roomVbox = QVBoxLayout()
        roomVbox.addWidget(self.rightBox1)
        roomVbox.addWidget(self.rightBox2)
        roomVbox.addWidget(self.rightBox3)
        rightGbox.setLayout(roomVbox)

        layout = QGridLayout()

        layout.addWidget(leftBox1, 0, 0, 3, 1)
        layout.addWidget(centerGbox, 0, 1)
        layout.addWidget(rightGbox, 0, 2, 3, 1)
        
        self.setLayout(layout)
        self.setWindowTitle('디아블로 매크로')
        self.setWindowIcon(QIcon('diablo_favicon.ico'))
        self.show()

    def CenterRadioButtonClicked(self):
        if self.centerRadio1.isChecked():
            self.jewelry.SetMonitorSize(100)
            self.room.SetMonitorSize(100)
        elif self.centerRadio11.isChecked():
            self.jewelry.SetMonitorSize(125)
            self.room.SetMonitorSize(125)
        elif self.centerRadio111.isChecked():
            self.jewelry.SetMonitorSize(150)
            self.room.SetMonitorSize(150)

    def RightRadioButtonClicked(self):
        if self.rightRadio1.isChecked():
            self.room.setDifficulty('normal')
        elif self.rightRadio11.isChecked():
            self.room.setDifficulty('nightmare')
        elif self.rightRadio111.isChecked():
            self.room.setDifficulty('hell')

    def RightRadioButtonClicked2(self):
        if self.rightRadio2.isChecked():
            self.room.setDifficulty2('normal')
        elif self.rightRadio22.isChecked():
            self.room.setDifficulty2('nightmare')
        elif self.rightRadio222.isChecked():
            self.room.setDifficulty2('hell')

    def RightRadioButtonClicked3(self):
        if self.rightRadio3.isChecked():
            self.room.setDifficulty3('normal')
        elif self.rightRadio33.isChecked():
            self.room.setDifficulty3('nightmare')
        elif self.rightRadio333.isChecked():
            self.room.setDifficulty3('hell')

    def RightBoxClicked(self):
        onMonitors = []
        if self.rightBox1.isChecked():
            onMonitors.append('first')
        if self.rightBox2.isChecked():
            onMonitors.append('second')
        if self.rightBox3.isChecked():
            onMonitors.append('third')

        self.room.SetOnMonitors(onMonitors)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = MyApp()
    
    sys.exit(app.exec_())
