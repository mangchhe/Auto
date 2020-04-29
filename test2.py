import tkinter as tk
from tkinter import *
from PIL import ImageGrab, Image, ImageOps
import cv2
import numpy as np
from ImageController import ImageController
import time

aa = ImageController()
g_x, g_y, g_w, g_h = aa.imageLocation('red house')  # 절대 좌표
diceBox = (g_x + 89, g_y + 444, g_x + 353, g_y + 600)

def isComb():
    img = ImageGrab.grab(
        bbox=(g_x + g_w - 20, g_y + g_h + 400, g_x + g_w + 20, g_y + g_h + 650))
    img.save('gd.png')
    img = ImageOps.grayscale(img)
    return np.array(Image.Image.getcolors(img)).sum() - 37000  # 36023


def isComb2():
    img = ImageGrab.grab(
        bbox=(g_x + g_w - 20, g_y + g_h + 365, g_x + g_w + 400, g_y + g_h + 375))
    img.save('gd.png')
    img = ImageOps.grayscale(img)

    return np.array(Image.Image.getcolors(img)).sum()  # 13662


while True:

    print(isComb2())
    time.sleep(1)


