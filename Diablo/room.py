from inactiveMacro import ImagePosExtract, GetWindowRect, DoubleLeftClick, LeftClick, ClickText, TypingTexts, GetHandleName
import time
import string
import random

class Room:

    def __init__(self):
        self._hwnd = 0
        self._hwnd2 = 0
        self._hwnd3 = 0
        self._LENGH = 10
        self._text = ''
        self._count = 1
        self._start = True

    def CreateRoomTitle(self):
        result = ''
        stringPool = string.ascii_lowercase + string.digits
        for i in range(self._LENGH):
            result += random.choice(stringPool)
        result += random.choice(string.ascii_lowercase)
        return result

    def FirstWindow(self):
        g_l, g_t, g_w, g_h = GetWindowRect(self._hwnd)
        ClickText(self._hwnd, '\x1b')
        LeftClick(self._hwnd, (g_w - g_l) // 2, (g_h - g_t) // 2)
        ClickText(self._hwnd2, '\x1b')
        LeftClick(self._hwnd2, (g_w - g_l) // 2, (g_h - g_t) // 2)
        ClickText(self._hwnd3, '\x1b')
        LeftClick(self._hwnd3, (g_w - g_l) // 2, (g_h - g_t) // 2)

        time.sleep(1.5)

        x, y = ImagePosExtract(self._hwnd, 'img/room/make.PNG')
        LeftClick(self._hwnd, x, y)
        x, y = ImagePosExtract(self._hwnd, 'img/room/gameName.PNG')
        DoubleLeftClick(self._hwnd, x, y + 20)
        TypingTexts(self._hwnd, self._text)
        x, y = ImagePosExtract(self._hwnd, 'img/room/gameMake.PNG')
        LeftClick(self._hwnd, x, y)

    def SecondWindow(self):
        x, y = ImagePosExtract(self._hwnd2, 'img/room/join.PNG')
        LeftClick(self._hwnd2, x, y)
        LeftClick(self._hwnd3, x, y)
        x, y = ImagePosExtract(self._hwnd2, 'img/room/gameName2.PNG')
        DoubleLeftClick(self._hwnd2, x, y + 20)
        DoubleLeftClick(self._hwnd3, x, y + 20)
        TypingTexts(self._hwnd2, self._text)
        TypingTexts(self._hwnd3, self._text)
        x, y = ImagePosExtract(self._hwnd2, 'img/room/gameJoin.PNG')
        LeftClick(self._hwnd2, x, y)
        LeftClick(self._hwnd3, x, y)

    def main(self):
        if self._start:
            self._hwnd = GetHandleName('D2Loader')
            self._hwnd2 = GetHandleName('D2Loader2')
            self._hwnd3 = GetHandleName('D2Loader3')
            self._text = self.CreateRoomTitle()
            self._start = False
            self._text = self._text + str(self._count)
        else:
            self._text = self._text + str(self._count)
            self._count += 1
        self.FirstWindow()
        self.SecondWindow()