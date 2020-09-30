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
        self.__monitors = 0
        self.__difficulty = 1
        self.__difficulty2 = 1
        self.__difficulty3 = 1

    def setDifficulty(self, num):
        self.__difficulty = num

    def setDifficulty2(self, num):
        self.__difficulty2 = num

    def setDifficulty3(self, num):
        self.__difficulty3 = num

    def getDifficulty(self):
        return self.__difficulty

    def getDifficulty2(self):
        return self.__difficulty2

    def getDifficulty3(self):
        return self.__difficulty3

    def CreateRoomTitle(self):
        random.seed(datetime.now())
        result = ''
        stringPool = string.ascii_lowercase + string.digits
        for i in range(self.__LENGH):
            result += random.choice(stringPool)
        result += random.choice(string.ascii_lowercase)
        return result

    def FirstWindow(self, text):
        g_l, g_t, g_w, g_h = GetWindowRect(self.__hwnd)
        ClickText(self.__hwnd, '\x1b')
        LeftClick(self.__hwnd, (g_w - g_l) // 2, (g_h - g_t) // 2)
        x, y = ImagePosExtract(self.__hwnd, 'img/room/make.PNG')
        LeftClick(self.__hwnd, x, y)
        x, y = ImagePosExtract(self.__hwnd, 'img/room/gameName.PNG')
        DoubleLeftClick(self.__hwnd, x, y + 20)
        TypingTexts(self.__hwnd, text)
        self.End()

    def SecondWindow(self, text):
        g_l, g_t, g_w, g_h = GetWindowRect(self.__hwnd2)
        ClickText(self.__hwnd2, '\x1b')
        LeftClick(self.__hwnd2, (g_w - g_l) // 2, (g_h - g_t) // 2)
        x, y = ImagePosExtract(self.__hwnd2, 'img/room/join.PNG')
        LeftClick(self.__hwnd2, x, y)
        x, y = ImagePosExtract(self.__hwnd2, 'img/room/gameName2.PNG')
        DoubleLeftClick(self.__hwnd2, x, y + 20)
        TypingTexts(self.__hwnd2, text)

    def ThirdWinodow(self, text):
        g_l, g_t, g_w, g_h = GetWindowRect(self.__hwnd3)
        ClickText(self.__hwnd3, '\x1b')
        LeftClick(self.__hwnd3, (g_w - g_l) // 2, (g_h - g_t) // 2)
        x, y = ImagePosExtract(self.__hwnd3, 'img/room/join.PNG')
        LeftClick(self.__hwnd3, x, y)
        x, y = ImagePosExtract(self.__hwnd3, 'img/room/gameName2.PNG')
        DoubleLeftClick(self.__hwnd3, x, y + 20)
        TypingTexts(self.__hwnd3, text)

    def End(self):
        x, y = ImagePosExtract(self.__hwnd, 'img/room/gameMake.PNG')
        
        if self.__monitors == 1:
            LeftClick(self.__hwnd, x, y)
        elif self.__monitors == 2:
            x, y = ImagePosExtract(self.__hwnd2, 'img/room/gameJoin.PNG')
            LeftClick(self.__hwnd, x, y)
            time.sleep(1)
            LeftClick(self.__hwnd2, x, y)
        elif self.__monitors == 3:
            x, y = ImagePosExtract(self.__hwnd2, 'img/room/gameJoin.PNG')
            x, y = ImagePosExtract(self.__hwnd3, 'img/room/gameJoin.PNG')
            LeftClick(self.__hwnd, x, y)
            time.sleep(1)
            LeftClick(self.__hwnd2, x, y)
            time.sleep(1)
            LeftClick(self.__hwnd3, x, y)

    def main(self):
        self.__hwnd = GetHandleName('D2Loader')
        self.__hwnd2 = GetHandleName('D2Loader2')
        self.__hwnd3 = GetHandleName('D2Loader3')

        self.__monitors = len(list(filter(lambda x : x != 0, [self.__hwnd, self.__hwnd2, self.__hwnd3])))

        if self.__start:
            self.__text = self.CreateRoomTitle()
            self.__start = False
            text = self.__text + str(self.__count)
            self.__count += 1
        else:
            text = self.__text + str(self.__count)
            self.__count += 1

        if self.__monitors == 1:
            thread = threading.Thread(target=self.FirstWindow, args=(text,))
            thread.start()
        elif self.__monitors == 2:
            thread = threading.Thread(target=self.FirstWindow, args=(text,))
            thread2 = threading.Thread(target=self.SecondWindow, args=(text,))
            thread.start()
            thread2.start()
        elif self.__monitors == 3:
            thread = threading.Thread(target=self.FirstWindow, args=(text,))
            thread2 = threading.Thread(target=self.SecondWindow, args=(text,))
            thread3 = threading.Thread(target=self.ThirdWinodow, args=(text,))
            thread.daemon = True
            thread2.daemon = True
            thread3.daemon = True
            thread.start()
            thread2.start()
            thread3.start()
        else:
            print('디아블로가 실행되어 있지 않습니다.')