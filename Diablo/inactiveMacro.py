import win32api
import win32gui
import win32con
import win32ui
import time
from ctypes import windll
from PIL import Image
import numpy as np
import cv2

def GetHandle():
    return win32gui.FindWindow('Diablo II', None)

def GetHandleName(name):
    return win32gui.FindWindow(None, name)

def GetWindowRect(hwnd):
    return win32gui.GetWindowRect(hwnd)

def MouseMove(handle, x, y):
    y -= 28
    lparam = win32api.MAKELONG(x, y)
    win32api.SendMessage(handle, win32con.WM_MOUSEMOVE, 0, lparam)

def LeftClick(handle, x, y):
    time.sleep(.15)
    MouseMove(handle, x, y)
    time.sleep(.15)
    y -= 28
    lparam = win32api.MAKELONG(x, y)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, 0, lparam) 
    time.sleep(.15)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, lparam)

def DoubleLeftClick(handle, x, y):
    MouseMove(handle, x, y)
    y -= 28
    lparam = win32api.MAKELONG(x, y)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, 0, lparam) 
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, lparam)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, 0, lparam) 
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, lparam)

def RightClick(handle, x, y):
    time.sleep(.15)
    lparam = win32api.MAKELONG(x, y)
    win32api.SendMessage(handle, win32con.WM_RBUTTONDOWN, 0, lparam) 
    time.sleep(.15)
    win32api.SendMessage(handle, win32con.WM_RBUTTONUP, 0, lparam)

def LRightClick(handle, x, y):
    LeftClick(handle, x, y)
    RightClick(handle, x, y)

def ClickText(handle, text):
    time.sleep(.15)
    win32api.SendMessage(handle, win32con.WM_KEYDOWN, ord(text), 0)
    win32api.SendMessage(handle, win32con.WM_KEYUP, ord(text), 0)

def TypingText(handle, text):
    time.sleep(.15)
    win32api.SendMessage(handle, win32con.WM_CHAR, ord(text), 0)

def TypingTexts(handle, texts):
    time.sleep(.15)
    for text in texts:
        win32api.SendMessage(handle, win32con.WM_CHAR, ord(text), 0)
    
def ImagesPosExtract(handle, path):
    left, top, right, bot = win32gui.GetWindowRect(handle)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(handle)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(handle, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(handle, hwndDC)

    img_rgb = np.array(im)
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    template = cv2.imread(path)
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .95
    loc = np.where(res >= threshold)
    imgsPos = []

    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        imgsPos.append([pt[0] + h//2, pt[1] + w//2])

    return imgsPos

def ImagePosExtract(handle, path):
    left, top, right, bot = win32gui.GetWindowRect(handle)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(handle)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(handle, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(handle, hwndDC)

    img_rgb = np.array(im)
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    template = cv2.imread(path)
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .95
    loc = np.where(res >= threshold)
    imgPos = []

    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        imgPos.append(pt[0] + h//2)
        imgPos.append(pt[1] + w//2)
        #cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (255,0,0), 0)
        break

    #img_rgb = Image.fromarray(img_rgb)
    #img_rgb.show()

    if imgPos:
        return imgPos
    else:
        return ImagePosExtract(handle, path)
