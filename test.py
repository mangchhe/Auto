import tkinter as tk
from tkinter import *
from PIL import ImageGrab, Image, ImageOps
import cv2
import numpy as np
from ImageController import ImageController

class App():

    def __init__(self, g_x, g_y, g_w, g_h, diceLookBox, diceBox, diceBoxCenter):
        self.root = tk.Tk()
        self.root.title('다이스 GUI')
        self.root.geometry('240x480+0+0')
        self.root.resizable(width=True, height=False)
        self.img = []
        self.labelImg = ['img' + str(i) for i in range(1, 16)]
        self.labelText = ['text' + str(i) for i in range(1, 16)]
        self.labelSimilarText = ['text' + str(i) for i in range(1, 16)]
        self.labelColor = ['white', 'black', 'red', 'blue', 'green', 'purple', 'yellow', 'pink']
        self.similarBox = []
        self.g_x = g_x
        self.g_y = g_y
        self.g_w = g_w
        self.g_h = g_h
        self.diceLookBox = diceLookBox
        self.diceBox = diceBox
        self.diceBoxCenter = diceBoxCenter
        self.diceBoxPixel = []

        for i in range(3):
            for j in range(5):
                self.img.append(PhotoImage(file='Image/' + 'dice_main' + '.PNG'))

        label = Label(self.root, text='Image', font=('맑은 고딕', 14, 'bold'), fg='white', bg="magenta")
        label.grid(row=0, columnspan=5)
        label = Label(self.root, text='RGB', font=('맑은 고딕', 14, 'bold'), fg='white', bg="magenta")
        label.grid(row=4, columnspan=5)
        label = Label(self.root, text='similar', font=('맑은 고딕', 14, 'bold'), fg='white', bg="magenta")
        label.grid(row=8, columnspan=5)

        for i in range(3):
            for j in range(5):
                self.labelImg[i * 5 + j] = Label(self.root, image=self.img[i * 5 + j])
                self.labelImg[i * 5 + j].grid(row=i + 1, column=j)
                self.labelText[i * 5 + j] = Label(self.root, text=str(i * 5 + j))
                self.labelText[i * 5 + j].grid(row=i + 5, column=j)
                self.labelSimilarText[i * 5 + j] = Label(self.root, text=str(i * 5 + j))
                self.labelSimilarText[i * 5 + j].grid(row=i + 9, column=j)

        self.updateDisplay()
        self.root.mainloop()

    def updateDisplay(self):

        if self.isComb() < 0 and self.isComb2() < 0:

            del self.img[:]
            del self.diceBoxPixel[:]
            self.seperateDiceImage()
            self.getSumPixel()
            self.pixelSimilarity()

            for i in range(3):
                for j in range(5):
                    self.img.append(PhotoImage(file='Image/case/' + str(i * 5 + j + 1) + '.PNG'))

            for i in range(3):
                for j in range(5):
                    self.labelImg[i * 5 + j].config(image=self.img[i * 5 + j])
                    R, G, B = self.diceBoxPixel[i * 5 + j]
                    self.labelText[i * 5 + j].config(text=str(R) + '\n' + str(G) + '\n' + str(B), font=('맑은 고딕', 9))
                    self.labelSimilarText[i * 5 + j].config(text=str(self.similarBox[i * 5 + j]), font=('맑은 고딕', 9), fg=self.labelColor[self.similarBox[i * 5 + j]])

        self.root.after(100, self.updateDisplay)

    def getSumPixel(self):  # 픽셀값 가져오기
        for i in range(1, 16):
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
            self.diceBoxPixel.append((R- 162000, G - 159300, B - 174600))

    def pixelSimilarity(self):
        self.similarBox = [0 for val in range(15)]
        similarNum = 1
        for i in range(0, 14):
            flag = False
            R, G, B = self.diceBoxPixel[i]
            if self.similarBox[i] != 0 or R+G+B == 0:
                continue
            for j in range(i + 1, 15):
                R2, G2, B2 = self.diceBoxPixel[j]
                if abs(R - R2) < 1100 and abs(G - G2) < 1100 and abs(B - B2) < 1100:
                    self.similarBox[i] = similarNum
                    self.similarBox[j] = similarNum
                    flag = True
            if flag:
                similarNum += 1

    def seperateDiceImage(self):
        img = ImageGrab.grab(bbox=self.diceBox)
        for i in range(15):
            img.crop(self.diceLookBox[i]).save('Image/case/' + str(i + 1) + '.PNG')

    def isCombDice(self, num):
        hurricain_2 = (29444, 28351, 10743)
        hurricain_3 = (28084, 26971, 3324)
        after_hurricain_2 = (28513, 11522, 4330)
        after_hurricain_3 = (26834, 3725, -6313)
        ice_2 = (31140, 20740, 12336)
        ice_3 = (30487, 14747, 2023)

        if self.compareImportantDice(num, hurricain_2) or self.compareImportantDice(num, hurricain_3) or self.compareImportantDice(num, ice_2) or self.compareImportantDice(num, ice_3) or self.compareImportantDice(num, after_hurricain_2) or self.compareImportantDice(num, after_hurricain_3):
            return False
        else:
            return True

    def compareImportantDice(self, num, tmp):
        if abs(self.diceBoxPixel[num][0] - tmp[0]) < 1500 and abs(self.diceBoxPixel[num][1] - tmp[1]) < 1500 and abs(self.diceBoxPixel[num][2] - tmp[2]) < 1500:
            return True

    def isComb(self):
        img = ImageGrab.grab(
            bbox=(self.g_x + self.g_w - 20, self.g_y + self.g_h + 400, self.g_x + self.g_w + 20, self.g_y + self.g_h + 650))
        img = ImageOps.grayscale(img)
        return np.array(Image.Image.getcolors(img)).sum() - 37000  # 36023

    def isComb2(self):
        img = ImageGrab.grab(
            bbox=(self.g_x + self.g_w - 20, self.g_y + self.g_h + 365, self.g_x + self.g_w + 400, self.g_y + self.g_h + 375))
        img = ImageOps.grayscale(img)

        return np.array(Image.Image.getcolors(img)).sum() - 15000  # 13662

if __name__ == '__main__':

    aa = ImageController()

    g_x, g_y, g_w, g_h = aa.imageLocation('red house')  # 절대 좌표
    diceBox = (g_x + 89, g_y + 444, g_x + 353, g_y + 600)
    diceLookBox = []
    diceBoxCenter = []

    screen = ImageGrab.grab(bbox=diceBox)
    img = np.array(screen)

    kernel = np.ones((5, 5), np.uint8)
    result = cv2.dilate(img, kernel, iterations=4)  # 팽창
    result = cv2.Canny(result, 50, 150)  # 엣지 검출
    result = cv2.bitwise_not(result)  # 색 반전
    contours = cv2.findContours(result.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # 엣지 강조
    cv2.drawContours(result, contours[0], -1, (0, 0, 0), 1)

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

        diceLookBox.append((center_x - 15, center_y - 15, center_x + 15, center_y + 15))
        diceBoxCenter.append((center_x, center_y))

    app = App(g_x, g_y, g_w, g_h, diceLookBox, diceBox, diceBoxCenter)
