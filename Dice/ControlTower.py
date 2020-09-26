from PIL import ImageGrab, Image, ImageOps
import pyautogui
import time
import cv2
import numpy as np
import threading
from DiceGui import App
from ImageController import ImageController
from CombineFlag import CombineFlag

class ControlTower(ImageController):

    def __init__(self):
        # config
        try:
            self.conf = .9
            pyautogui.FAILSAFE = False
            self.g_x, self.g_y, self.g_w, self.g_h = self.imageLocation('red house')  # 절대 좌표
            self.diceBox = (self.g_x + 89, self.g_y + 444, self.g_x + 353, self.g_y + 600)
            self.diceLookBox = []
            self.diceBoxCenter = []
            self.combineFlag = CombineFlag()
        except:
            print('not found red house')

    def adAction(self): # 광고 보기
        print('광고 보기')
        time.sleep(1)
        self.imageClickRepeat(self.imagePath('ad2'))
        if self.imageRecognize(self.imagePath('ad wait')):
            self.imageClick(self.imagePath('ad ok'))
        else:
            pass
        time.sleep(50)
        pyautogui.press('esc')
        time.sleep(3)
        if not self.imageRecognize(self.imagePath('start')):
            self.reconnect()
        breakCount = 0
        while True:
            if breakCount == 30:
                break
            if self.imageRecognize(self.imagePath('start')):
                break
            if self.imageRecognize(self.imagePath('ad2')):
                break
            else:
                breakCount += 1
                time.sleep(1)

        print('광고 끝')

    def adAction2(self):
        print('광고 보기')
        while True:
            if self.imageRecognize(self.imagePath('ad_dia')):
                self.imageClickRepeat(self.imagePath('ad_dia'))
                self.imageClickRepeat(self.imagePath('ad_dia2'))
                time.sleep(3)
                break
            else:
                if controlTower.imageRecognize(controlTower.imagePath('start')):
                    time.sleep(3)
                    break
        print('광고 끝')

    def reconnect(self):
        x, y, w, h = pyautogui.locateOnScreen(self.imagePath('ad_err1'))
        pyautogui.click(x + w, y)
        self.imageClickRepeat(self.imagePath('ad_err2'))

    def diceUpgrade(self, num): # 다이스 업그레이드
        pyautogui.click(self.g_x + 32 + (68 * num), self.g_y + 754 + 33, clicks=1)

    def diceCaseConf(self): # 다이스 판 위치 설정
        screen = ImageGrab.grab(bbox=self.diceBox)
        img = np.array(screen)

        kernel = np.ones((5,5), np.uint8)
        result = cv2.dilate(img, kernel, iterations=4) # 팽창
        result = cv2.Canny(result, 50, 150) # 엣지 검출
        result = cv2.bitwise_not(result) # 색 반전
        contours = cv2.findContours(result.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # 엣지 강조
        cv2.drawContours(result, contours[0], -1, (0,0,0), 1)

        nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(result)

        for i in range(nlabels):

            if i < 2:
                continue

            area = stats[i, cv2.CC_STAT_AREA]
            center_x = int(centroids[i, 0])
            center_y = int(centroids[i, 1])
            left = stats[i, cv2.CC_STAT_LEFT]
            top = stats[i, cv2.CC_STAT_TOP]
            width = stats[i, cv2.CC_STAT_WIDTH]
            height = stats[i, cv2.CC_STAT_HEIGHT]

            self.diceLookBox.append((center_x-15,center_y-15,center_x+15,center_y+15))
            self.diceBoxCenter.append((center_x,center_y))

    def isComb(self):
        img = ImageGrab.grab(bbox=(self.g_x + self.g_w - 20, self.g_y + self.g_h + 400, self.g_x + self.g_w + 20, self.g_y + self.g_h + 650))
        img = ImageOps.grayscale(img)
        return np.array(Image.Image.getcolors(img)).sum() - 37000 # 32000

    def isComb2(self):
        img = ImageGrab.grab(
            bbox=(self.g_x + self.g_w - 20, self.g_y + self.g_h + 365, self.g_x + self.g_w + 400, self.g_y + self.g_h + 375))
        img = ImageOps.grayscale(img)
        return np.array(Image.Image.getcolors(img)).sum() - 15000 # 10000

    def sendKatalk(self, msg):
        try:
            self.imageClick(self.imagePath('katalk chat'))
            pyautogui.write(msg, interval=.1)
            self.imageClick(self.imagePath('katalk send'))
        except:
            pass

    def execute(self):# GUI(스레드)
        self.app = App(self.g_x, self.g_y, self.g_w, self.g_h, self.diceLookBox, self.diceBox, self.diceBoxCenter, self.combineFlag)

    def getFlag(self):

        return self.combineFlag.getFlag()

    def setFlag(self, judge):

        self.combineFlag.setFlag(judge)

    def initTime(self):

        self.combineFlag.initTime()

    def initTimeGrade(self):

        self.combineFlag.initTimeGrade()

    def plusTimeGrade(self):

        self.combineFlag.plusTimeGrade()

    def sendimti(self):

        while True:

            if controlTower.imageRecognize(controlTower.imagePath('imti')):
                controlTower.imageClickRepeat(controlTower.imagePath('imti'))
                break

            time.sleep(.1)

        while True:

            if controlTower.imageRecognize(controlTower.imagePath('imti2')):
                controlTower.imageClickRepeat(controlTower.imagePath('imti2'))
                break

            time.sleep(.1)



if __name__ == '__main__':

    countTmp = 0
    playCount = 0
    controlTower = ControlTower()

    while True:

        flag = False

        t = threading.Thread(target=controlTower.execute)

        print('실행 횟수 :',playCount)

        print('매크로 시작')
        #-------------------------------------
        while True:
            time.sleep(2)
            if controlTower.imageRecognize(controlTower.imagePath('start')):
                controlTower.imageClickRepeat(controlTower.imagePath('start'))
                break
            else:
                controlTower.adAction()

        print('퀵 매치 시작')
        # -------------------------------------
        while True:
            if controlTower.imageRecognize(controlTower.imagePath('quick match')):
                controlTower.imageClickRepeat(controlTower.imagePath('quick match'))
                break

        print('다이스 판 설정')
        # -------------------------------------
        if countTmp == 0:
            while True:
                if pyautogui.locateCenterOnScreen(controlTower.imagePath('create dice'), confidence=controlTower.conf) != None:
                    controlTower.diceCaseConf()
                    t.start()
                    countTmp += 1
                    break
                else:
                    time.sleep(1)
        else:
            breakCount = 0
            while True:
                if breakCount == 15:
                    flag = True
                    break
                if pyautogui.locateCenterOnScreen(controlTower.imagePath('create dice'), confidence=controlTower.conf) != None:
                    controlTower.initTime()
                    controlTower.initTimeGrade()
                    break
                else:
                    breakCount += 1
                    time.sleep(1)
        if flag:
            continue

        print('게임 진행...')
        # -------------------------------------
        x, y = pyautogui.locateCenterOnScreen(controlTower.imagePath('create dice'), confidence = .9)
        pyautogui.click(x,y,clicks=10,interval=.1)

        controlTower.sendimti()

        while True:
            if controlTower.imageClick(controlTower.imagePath('end ok')):
                playCount += 1
                print('게임 끝')
                time.sleep(7)
                controlTower.plusTimeGrade()
                break
            if controlTower.imageRecognize(controlTower.imagePath('fight')) and controlTower.imageRecognize(controlTower.imagePath('fight2')):  # err
                controlTower.imageClick(controlTower.imagePath('fight'))
                playCount += 1
                print('게임 끝')
                time.sleep(2)
                controlTower.plusTimeGrade()
                break

            if (controlTower.isComb() > 0 or controlTower.isComb2() > 0) and controlTower.imageRecognize(controlTower.imagePath('create dice')) and controlTower.getFlag():
                controlTower.diceUpgrade(1)
                if controlTower.imageRecognize(controlTower.imagePath('create dice')):
                    controlTower.imageClick(controlTower.imagePath('create dice'))
                #time.sleep(.3)