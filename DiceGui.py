import tkinter as tk
from tkinter import *
from PIL import Image, ImageOps, ImageGrab
import cv2
import numpy as np
import time
import pyautogui
import random as rd
import os
from Auto.ImageController import ImageController

class App(ImageController):

    def __init__(self, g_x, g_y, g_w, g_h, diceLookBox, diceBox, diceBoxCenter):
        self.root = tk.Tk()
        self.similarBox = []
        self.g_x = g_x
        self.g_y = g_y
        self.g_w = g_w
        self.g_h = g_h
        self.diceLookBox = diceLookBox
        self.diceBox = diceBox
        self.diceBoxCenter = diceBoxCenter
        self.diceBoxPixel = []

        self.updateDisplay()
        self.root.mainloop()

    def updateDisplay(self):

        if self.isComb() < 0 and self.imageRecognize(self.imagePath('create dice')):  # 광고에서 0 이하인게 나오기 때문에 방지하기 위해서 이미지 식별도 추가
            time.sleep(1)
            del self.diceBoxPixel[:]
            self.seperateDiceImage()
            self.getSumPixel()
            self.pixelSimilarity()
            self.combiDice()

        self.root.after(500, self.updateDisplay)


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
            self.diceBoxPixel.append((R - 197100,G - 197100,B - 197100))


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
                if abs(R-R2) < 1100 and abs(G-G2) < 1100 and abs(B-B2) < 1100:
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
        return np.array(Image.Image.getcolors(img)).sum() - 22850

    def isComb2(self):
        img = ImageGrab.grab(
            bbox=(self.g_x + self.g_w - 20, self.g_y + self.g_h + 335, self.g_x + self.g_w + 380, self.g_y + self.g_h + 360))
        img = ImageOps.grayscale(img)
        return np.array(Image.Image.getcolors(img)).sum()

    def diceMove(self, x, y, goal_x, goal_y):
        rd_val = int(rd.random() * 10) - int(rd.random() * 10)
        rd_val2 = int(rd.random() * 10) - int(rd.random() * 10)
        pyautogui.moveTo(x=x, y=y)
        pyautogui.dragTo(goal_x + rd_val, goal_y + rd_val2, .5)
    
    def combiDice(self):
        for i in range(14):
            if self.isComb() > 0:
                print('조합 중지')
                break
            if self.similarBox[i] != 0 and self.isCombDice(i):
                try:
                    j = self.similarBox.index(self.similarBox[i],i+1)
                except:
                    self.similarBox[i] = 0
                    break
                x, y = self.diceBoxCenter[i]
                goal_x, goal_y = self.diceBoxCenter[j]
                self.diceMove(x + self.g_x + 89, y + self.g_y + 444, goal_x + self.g_x + 89, goal_y + self.g_y + 444)
                self.similarBox[i] = 0
                self.similarBox[j] = 0
                break
            elif sum(self.similarBox) == 0:
                break

    def isCombDice(self, num):
        hurricain_1 = (30802,29490,16798)
        hurricain_2 = (29444,28351,10743)
        hurricain_3 = (28084,26971,3324)
        after_hurricain_1 = (29421,16000,13573)
        after_hurricain_2 = (28513,11522,4330)
        after_hurricain_3 = (26834,3725,-6313)
        #ice_2 = (31140, 20740, 12336)
        ice_3 = (30487, 14747, 2023)

        if self.compareImportantDice(num, hurricain_1) or self.compareImportantDice(num, hurricain_2) or self.compareImportantDice(num, hurricain_3) or self.compareImportantDice(num, ice_3) or self.compareImportantDice(num, after_hurricain_1) or self.compareImportantDice(num, after_hurricain_2) or self.compareImportantDice(num, after_hurricain_3):
            return False
        else:
            return True

    def compareImportantDice(self, num, tmp):
        if abs(self.diceBoxPixel[num][0] - tmp[0]) < 3000 and abs(self.diceBoxPixel[num][1] - tmp[1]) < 3000 and abs(self.diceBoxPixel[num][2] - tmp[2]) < 3000:
            return True