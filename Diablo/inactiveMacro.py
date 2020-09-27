import win32api
import win32gui
import win32con
import time

def MouseMove(handle, y, x, t, l):
    y -= 28
    lparam = win32api.MAKELONG(x - l, y - t)
    win32api.SendMessage(handle, win32con.WM_MOUSEMOVE, 0, lparam)

def LeftClick(handle, y, x, t, l):
    time.sleep(.15)
    MouseMove(handle, y, x, t, l)
    time.sleep(.15)
    y -= 28
    lparam = win32api.MAKELONG(x - l, y - t)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, 0, lparam) 
    time.sleep(.15)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, lparam)

def RightClick(handle, y, x, t, l):
    time.sleep(.15)
    lparam = win32api.MAKELONG(x - l, y - t)
    win32api.SendMessage(handle, win32con.WM_RBUTTONDOWN, 0, lparam) 
    time.sleep(.15)
    win32api.SendMessage(handle, win32con.WM_RBUTTONUP, 0, lparam)

def LRightClick(handle, y, x, t, l):
    LeftClick(handle, y, x, t, l)
    RightClick(handle, y, x, t, l)
    
