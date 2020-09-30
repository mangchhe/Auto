"""
    작성일 : 20/09/27
"""

import time
import inactiveMacro
import threading

jewelrys = ['diamond', 'amethyst', 'emerald', 'ruby', 'sapphire', 'skull', 'topaz']
g_l, g_t, g_w, g_h, hwnd = 0, 0, 0, 0, 0

""" 
    보석 개수 찾기
    로직 : 개수가 3개 이상일 경우 짝을 지어 묶어 반환
    @return 각 보석 위치
"""

class Jewelry:

    def findJewelryNum(self):

        jewelrysPos = []

        for i, jewelry in enumerate(jewelrys):
            
            data = inactiveMacro.ImagesPosExtract(hwnd, 'img/jewelry/' + jewelry + '.PNG')
            jewelrysPos.append([])

            if len(data) > 2:
                print(jewelry, str(len(data)) + '개', '찾음')
                for j in range(3 * (len(data) // 3)):
                    x, y = data[j]
                    jewelrysPos[i].append([x,y])
            else:
                print(jewelry, str(3 - len(data)) + '개', '부족')

        return jewelrysPos
        
    def findJewelryNum2(self):

        jewelrysPos = []

        for i, jewelry in enumerate(jewelrys):
            jewelrysPos.extend(inactiveMacro.ImagesPosExtract(hwnd, 'img/jewelry/' + jewelry + '.PNG'))
        return jewelrysPos

    def findJewelryNum3(self, jewelrysPos, jewelrysPos2):

        tmp = []

        for i in jewelrysPos:
            for j in i:
                tmp.append(j)

        for i in range(len(jewelrysPos2)-1, -1, -1):
            if jewelrysPos2[i] in tmp:
                del jewelrysPos2[i]

        return jewelrysPos2

    """
        큐브와 조합버튼 찾기
        @return 큐브, 조합버튼 위치
    """
    def findEtc(self):

        combineBtn = inactiveMacro.ImagePosExtract(hwnd, 'img/function/combine.PNG')
        cube = inactiveMacro.ImagePosExtract(hwnd, 'img/boxs/cube.PNG')
        jewelryBox = inactiveMacro.ImagePosExtract(hwnd, 'img/boxs/jewelryBox.PNG')
        cubeCorner = inactiveMacro.ImagePosExtract(hwnd, 'img/etc/cubeCorner.PNG')

        return combineBtn, cube, jewelryBox, cubeCorner

    """
        쥬얼 합성
    """
    def moveFindedJewelry(self, jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner):

        if combineBtn and cube and jewelryBox:
            for jewelryPos in jewelrysPos:
                if jewelryPos:
                    count = 0
                    for x, y in jewelryPos:
                        inactiveMacro.LRightClick(hwnd, x, y)
                        count += 1
                        if count == 3:
                            inactiveMacro.LeftClick(hwnd, combineBtn[0], combineBtn[1])
                            inactiveMacro.LRightClick(hwnd, jewelryBox[0], jewelryBox[1])
                            inactiveMacro.LeftClick(hwnd, combineBtn[0], combineBtn[1])
                            inactiveMacro.LeftClick(hwnd, cubeCorner[0], cubeCorner[1])
                            inactiveMacro.LeftClick(hwnd, jewelryBox[0], jewelryBox[1])
                            count = 0
        else:
            if not combineBtn:
                print('조합버튼을 찾기 못했습니다.')
            if not cube:
                print('큐브를 찾기 못했습니다.')
            if not jewelryBox:
                print('보석상자를 찾기 못했습니다.')

    def moveFindedJewelry2(self, jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner):

        flag = True
        if combineBtn and cube and jewelryBox:
            for jewelryPos in jewelrysPos:
                x, y = jewelryPos
                inactiveMacro.LRightClick(hwnd, x, y)
                if flag:
                    inactiveMacro.LRightClick(hwnd, jewelryBox[0], jewelryBox[1])
                    flag = False
                inactiveMacro.LeftClick(hwnd, combineBtn[0], combineBtn[1])
            inactiveMacro.LeftClick(hwnd, cubeCorner[0], cubeCorner[1])
            inactiveMacro.LeftClick(hwnd, jewelryBox[0], jewelryBox[1])
        else:
            if not combineBtn:
                print('조합버튼을 찾기 못했습니다.')
            if not cube:
                print('큐브를 찾기 못했습니다.')
            if not jewelryBox:
                print('보석상자를 찾기 못했습니다.')

    """
        보석 합성 메인
    """
    def jewelryCombineMain(self):
        thread = threading.Thread(target=self.execute)
        thread.daemon = True
        thread.start()

    def jewelryCombineMain2(self):
        thread = threading.Thread(target=self.execute2)
        thread.daemon = True
        thread.start()

    def jewelryCombineMain3(self):
        thread = threading.Thread(target=self.execute3)
        thread.daemon = True
        thread.start()

    def execute(self):
        global g_l, g_t, g_w, g_h, hwnd
        try:
            hwnd = inactiveMacro.GetHandleName('D2Loader')
            g_l, g_t, g_w, g_h = inactiveMacro.GetWindowRect(hwnd)
            combineBtn, cube, jewelryBox, cubeCorner = self.findEtc()
            jewelrysPos = self.findJewelryNum()
            moveFindedJewelry(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner)
        except:
            print('디아블로가 실행되어 있지 않습니다.')

    def execute2(self):
        global g_l, g_t, g_w, g_h, hwnd

        try:
            hwnd = inactiveMacro.GetHandleName('D2Loader')
            g_l, g_t, g_w, g_h = inactiveMacro.GetWindowRect(hwnd)
            combineBtn, cube, jewelryBox, cubeCorner = self.findEtc()
            jewelrysPos = self.findJewelryNum2()
            moveFindedJewelry2(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner)
        except:
            print('디아블로가 실행되어 있지 않습니다.')

    def execute3(self):
        global g_l, g_t, g_w, g_h, hwnd

        try:
            hwnd = inactiveMacro.GetHandleName('D2Loader')
            g_l, g_t, g_w, g_h = inactiveMacro.GetWindowRect(hwnd)
            combineBtn, cube, jewelryBox, cubeCorner = self.findEtc()
            jewelrysPos = self.findJewelryNum()
            jewelrysPos2 = self.findJewelryNum2()
            jewelrysPos3 = self.findJewelryNum3(jewelrysPos, jewelrysPos2)
            moveFindedJewelry(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner)
            moveFindedJewelry2(jewelrysPos3, combineBtn, cube, jewelryBox, cubeCorner)
        except:
            print('디아블로가 실행되어 있지 않습니다.')