import tkinter as tk
from tkinter import *
from PIL import Image, ImageOps, ImageGrab
import cv2
import numpy as np
import time
import pyautogui
import random as rd
import os
from ImageController import ImageController

class App(ImageController):

    def __init__(self, g_x, g_y, g_w, g_h, diceLookBox, diceBox, diceBoxCenter, combineFlag):
        self.root = tk.Tk()
        # GUI

        # Combine
        self.similarBox = []
        self.g_x = g_x
        self.g_y = g_y
        self.g_w = g_w
        self.g_h = g_h
        self.diceLookBox = diceLookBox
        self.diceBox = diceBox
        self.diceBoxCenter = diceBoxCenter
        self.combineFlag = combineFlag
        self.diceBoxPixel = []
        self.diceNoCombineList = []

        self.updateDisplay()
        self.root.mainloop()

    def updateDisplay(self):

        if self.isComb() < 0 and self.isComb2() < 0 and self.imageRecognize(self.imagePath('create dice')) and self.combineFlag:  # 광고에서 0 이하인게 나오기 때문에 방지하기 위해서 이미지 식별도 추가
            #time.sleep(.3)
            print('조합 시작')
            self.combineFlag.setFlag(False)

            if self.combineFlag.getTimeGrade() != 2:
                self.noConbineAction()

            del self.diceBoxPixel[:]
            self.seperateDiceImage()
            self.getSumPixel()
            self.pixelSimilarity()
            self.combiDice()

            self.combineFlag.setFlag(True)

        self.root.after(100, self.updateDisplay)

    def noConbineAction(self):

        if self.combineFlag.getTimeGrade() == 0:

            del self.diceNoCombineList[:]

            print('현재 1단계')

            self.diceNoCombineList.append([65883, 67295, 39611]) # hurricain_1
            self.diceNoCombineList.append([64546, 66114, 33308]) # hurricain 2
            self.diceNoCombineList.append([63124, 64689, 25583])  # hurricain 3
            self.diceNoCombineList.append([61813, 63403, 18602])  # hurricain 4
            self.diceNoCombineList.append([60374, 61975, 10845])  # hurricain 5
            self.diceNoCombineList.append([59088, 60685, 3848])  # hurricain 6
            self.diceNoCombineList.append([65320, 66691, 37147])  # hurricain 7

            self.diceNoCombineList.append([65261, 55784, 35779])   # after_hurricain 1
            self.diceNoCombineList.append([63675, 49283, 26868])   # after_hurricain 2
            self.diceNoCombineList.append([61532, 39836, 14858])  # after_hurricain 3
            self.diceNoCombineList.append([60335, 33835, 5756])  # after_hurricain 4
            self.diceNoCombineList.append([58557, 25668, -5388])  # after_hurricain 5
            self.diceNoCombineList.append([56989, 18333, -15384])  # after_hurricain 6
            self.diceNoCombineList.append([64678, 53679, 32981])  # after_hurricain 7

            self.diceNoCombineList.append([57639, 42998, 30859]) # grow1
            self.diceNoCombineList.append([52060, 35183, 23461]) # grow2
            self.diceNoCombineList.append([45686, 25523, 14363]) # grow3
            self.diceNoCombineList.append([40211, 17501, 6789]) # grow4
            self.diceNoCombineList.append([33467, 7174, -2898]) # grow5
            self.diceNoCombineList.append([29427, 3427, -6644]) # grow6
            self.diceNoCombineList.append([49961, 36071, 23786]) # grow7

            self.combineFlag.plusTimeGrade()

        elif self.combineFlag.getTimeGrade() == 1 and self.combineFlag.getTime() > 240:

            print('현재 2단계')

            del self.diceNoCombineList[0:2]
            del self.diceNoCombineList[5:7]

            self.combineFlag.plusTimeGrade()

    def getSumPixel(self):  # 픽셀값 가져오기
        for i in range(1,16):
            img = Image.open('Image/case/' + str(i) + '.PNG')
            x, y = img.size
            img = np.array(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            R, G, B = 0, 0, 0
            for m in range(x):
                for n in range(y):
                    R += img[m][n][0]
                    G += img[m][n][1]
                    B += img[m][n][2]

            self.diceBoxPixel.append((R - 162000, G - 159300, B - 174600))

    def pixelSimilarity(self):
        self.similarBox = [0 for val in range(15)]
        similarNum = 1
        for i in range(0, 14):
            flag = False
            R, G, B = self.diceBoxPixel[i]
            if self.similarBox[i] != 0 or R == 0:
                continue
            for j in range(i+1,15):
                R2, G2, B2 = self.diceBoxPixel[j]
                if abs(R-R2) < 500 and abs(G-G2) < 500 and abs(B-B2) < 500:
                    self.similarBox[i] = similarNum
                    self.similarBox[j] = similarNum
                    flag = True
            if flag:
                similarNum += 1

    def seperateDiceImage(self):
        img = ImageGrab.grab(bbox=self.diceBox)
        for i in range(15):
            img.crop(self.diceLookBox[i]).save('Image/case/' + str(i + 1) + '.PNG')

    def isComb(self):
        img = ImageGrab.grab(bbox=(self.g_x + self.g_w - 20, self.g_y + self.g_h + 400, self.g_x + self.g_w + 20, self.g_y + self.g_h + 650))
        img = ImageOps.grayscale(img)
        return np.array(Image.Image.getcolors(img)).sum() - 37000 # 32000 # 22850

    def isComb2(self):
        img = ImageGrab.grab(
            bbox=(self.g_x + self.g_w - 20, self.g_y + self.g_h + 365, self.g_x + self.g_w + 400, self.g_y + self.g_h + 375))
        img = ImageOps.grayscale(img)
        return np.array(Image.Image.getcolors(img)).sum() - 15000 # 10000

    def diceMove(self, x, y, goal_x, goal_y):
        rd_val = int(rd.random() * 10) - int(rd.random() * 10)
        rd_val2 = int(rd.random() * 10) - int(rd.random() * 10)
        pyautogui.moveTo(x=x, y=y)
        pyautogui.dragTo(goal_x + rd_val, goal_y + rd_val2, .5)
    
    def combiDice(self):
        for i in range(14):
            print(i)
            #if self.imageRecognize(self.imagePath('end ok')):
            #    break
            if self.similarBox[i] != 0 and self.isCombDice(i):
                try:
                    j = self.similarBox.index(self.similarBox[i],i+1)
                    print('찾음')
                except:
                    self.similarBox[i] = 0
                    # break
                    print('못 찾음')
                    continue
                x, y = self.diceBoxCenter[i]
                goal_x, goal_y = self.diceBoxCenter[j]
                self.diceMove(x + self.g_x + 89, y + self.g_y + 444, goal_x + self.g_x + 89, goal_y + self.g_y + 444)
                self.similarBox[i] = 0
                self.similarBox[j] = 0
                # break
            elif sum(self.similarBox) == 0:
                print('합 0')
                break

    def isCombDice(self, num):
        for i in range(len(self.diceNoCombineList)):
                if abs(self.diceBoxPixel[num][0] - self.diceNoCombineList[i][0]) < 2000 and abs(self.diceBoxPixel[num][1] - self.diceNoCombineList[i][1]) < 2000 and abs(self.diceBoxPixel[num][2] - self.diceNoCombineList[i][2]) < 2000:
                    return False
        return True