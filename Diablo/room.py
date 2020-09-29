from inactiveMacro import ImagePosExtract, GetWindowRect, DoubleLeftClick, LeftClick, ClickText, TypingTexts, GetHandleName
import time
import string
import random
import threading
from datetime import datetime

class Room:

    def __init__(self):
        self.__hwnd = 0
        self.__hwnd2 = 0
        self.__hwnd3 = 0
        self.__LENGH = 8
        self.__text = ''
        self.__count = 0
        self.__start = True

    def CreateRoomTitle(self):
        random.seed(datetime.now())
        result = ''
        stringPool = string.ascii_lowercase + string.digits
        for i in range(self.__LENGH):
            result += random.choice(stringPool)
        result += random.choice(string.ascii_lowercase)
        return result

    def FirstWindow(self):
        g_l, g_t, g_w, g_h = GetWindowRect(self.__hwnd)
        ClickText(self.__hwnd, '\x1b')
        LeftClick(self.__hwnd, (g_w - g_l) // 2, (g_h - g_t) // 2)
        x, y = ImagePosExtract(self.__hwnd, 'img/room/make.PNG')
        LeftClick(self.__hwnd, x, y)
        x, y = ImagePosExtract(self.__hwnd, 'img/room/gameName.PNG')
        DoubleLeftClick(self.__hwnd, x, y + 20)
        TypingTexts(self.__hwnd, self.__text)

    def SecondWindow(self):
        g_l, g_t, g_w, g_h = GetWindowRect(self.__hwnd2)
        ClickText(self.__hwnd2, '\x1b')
        LeftClick(self.__hwnd2, (g_w - g_l) // 2, (g_h - g_t) // 2)
        x, y = ImagePosExtract(self.__hwnd2, 'img/room/join.PNG')
        LeftClick(self.__hwnd2, x, y)
        x, y = ImagePosExtract(self.__hwnd2, 'img/room/gameName2.PNG')
        DoubleLeftClick(self.__hwnd2, x, y + 20)
        TypingTexts(self.__hwnd2, self.__text)

    def ThirdWinodow(self):
        g_l, g_t, g_w, g_h = GetWindowRect(self.__hwnd3)
        ClickText(self.__hwnd3, '\x1b')
        LeftClick(self.__hwnd3, (g_w - g_l) // 2, (g_h - g_t) // 2)
        x, y = ImagePosExtract(self.__hwnd3, 'img/room/join.PNG')
        LeftClick(self.__hwnd3, x, y)
        x, y = ImagePosExtract(self.__hwnd3, 'img/room/gameName2.PNG')
        DoubleLeftClick(self.__hwnd3, x, y + 20)
        TypingTexts(self.__hwnd3, self.__text)

        self.End()

    def End(self):
        x, y = ImagePosExtract(self.__hwnd, 'img/room/gameMake.PNG')
        x, y = ImagePosExtract(self.__hwnd2, 'img/room/gameJoin.PNG')
        x, y = ImagePosExtract(self.__hwnd3, 'img/room/gameJoin.PNG')
        LeftClick(self.__hwnd, x, y)
        time.sleep(1)
        LeftClick(self.__hwnd2, x, y)
        time.sleep(1)
        LeftClick(self.__hwnd3, x, y)

    def main(self):
        if self.__start:
            self.__hwnd = GetHandleName('D2Loader')
            self.__hwnd2 = GetHandleName('D2Loader2')
            self.__hwnd3 = GetHandleName('D2Loader3')
            self.__text = self.CreateRoomTitle()
            self.__start = False
            self.__text = self.__text + str(self.__count)
            self.__count += 1
        else:
            self.__text = self.__text + str(self.__count)
            self.__count += 1

        thread = threading.Thread(target=self.FirstWindow)
        thread2 = threading.Thread(target=self.SecondWindow)
        thread3 = threading.Thread(target=self.ThirdWinodow)
        thread.daemon = True
        thread2.daemon = True
        thread3.daemon = True
        thread.start()
        thread2.start()
        thread3.start()