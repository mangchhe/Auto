import abc
import pyautogui
import time
import os

class ImageController(metaclass=abc.ABCMeta):

    def imageRecognize(self, imagePath):  # 이미지 탐색
        location = pyautogui.locateCenterOnScreen(imagePath, confidence = .9)
        try:
            x, y = location
            return 1
        except:
            return 0

    def imageClick(self, imagePath):  # 이미지 클릭하기
        location = pyautogui.locateCenterOnScreen(imagePath, confidence = .9)
        try:
            x, y = location
            pyautogui.click(x, y, clicks=1)
            return 1
        except:
            return 0

    def imageClickRepeat(self, imagePath):  # 이미지 클릭하기(반복)
        location = pyautogui.locateCenterOnScreen(imagePath, confidence = .9)
        try:
            x, y = location
            pyautogui.click(x, y, clicks=1)
        except:
            time.sleep(1)
            self.imageClickRepeat(imagePath)

    def imagePath(self, imageName):   # 이미지 절대경로 불러오기
        return os.path.dirname(os.path.realpath(__file__)) + '/Image/' + imageName + '.PNG'

    def imageLocation(self, imageName):   # 이미지 화면좌표 불러오기
        left, top, width, height = pyautogui.locateOnScreen(self.imagePath(imageName), confidence = .9)
        return left, top, width, height