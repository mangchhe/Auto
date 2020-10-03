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

    def __init__(self):
        self.__monitorSize = 100
        self.__adjustMonitorSize = {100:0, 125:.25, 150:.5}
        self.combineBtn = []
        self.cube = []
        self.jewelryBox = []
        self.cubeCorner = []
        self.adjustCombineBtn = [0, 0]
        self.adjustJewelryBox = [0, 0]
        self.adjustCubeCorner = [0, 0]
        self.adjustCube = [0, 0]

    def SetMonitorSize(self, size):
        self.__monitorSize = size
        
    def SetPosThroughMonitor(self):
        self.adjustCube = [int(self.cube[0] * self.__adjustMonitorSize[self.__monitorSize]), int(self.cube[1] * self.__adjustMonitorSize[self.__monitorSize])]
        self.adjustCombineBtn = [int(self.combineBtn[0] * self.__adjustMonitorSize[self.__monitorSize]), int(self.combineBtn[1] * self.__adjustMonitorSize[self.__monitorSize])]
        self.adjustJewelryBox = [int(self.jewelryBox[0] * self.__adjustMonitorSize[self.__monitorSize]), int(self.jewelryBox[1] * self.__adjustMonitorSize[self.__monitorSize])]
        self.adjustCubeCorner = [int(self.cubeCorner[0] * self.__adjustMonitorSize[self.__monitorSize]), int(self.cubeCorner[1] * self.__adjustMonitorSize[self.__monitorSize])]

    def findJewelryNum(self):

        jewelrysPos = []

        for i, jewelry in enumerate(jewelrys):
            
            data = inactiveMacro.ImagesPosExtract(hwnd, 'img/jewelry/' + jewelry + '.PNG')
            jewelrysPos.append([])

            if len(data) > 2:
                for j in range(3 * (len(data) // 3)):
                    x, y = data[j]
                    jewelrysPos[i].append([x,y])
            else:
                pass

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
        inactiveMacro.ClickText(hwnd, 'I')
        self.cube = inactiveMacro.ImagePosExtract(hwnd, 'img/boxs/cube.PNG')
        self.jewelryBox = inactiveMacro.ImagePosExtract(hwnd, 'img/boxs/jewelryBox.PNG')
        inactiveMacro.RightClick(hwnd, self.cube[0] + self.adjustCube[0], self.cube[1] + self.adjustCube[1])

    def findEtc2(self):
        self.combineBtn = inactiveMacro.ImagePosExtract(hwnd, 'img/function/combine.PNG')
        self.cubeCorner = inactiveMacro.ImagePosExtract(hwnd, 'img/etc/cubeCorner.PNG')
    """
        쥬얼 합성
    """
    def moveFindedJewelry(self, jewelrysPos):

        if self.combineBtn and self.cube and self.jewelryBox:
            for jewelryPos in jewelrysPos:
                if jewelryPos:
                    count = 0
                    for x, y in jewelryPos:
                        inactiveMacro.LRightClick(hwnd, x + int(x * self.__adjustMonitorSize[self.__monitorSize]), y + int(y * self.__adjustMonitorSize[self.__monitorSize]))
                        count += 1
                        if count == 3:
                            inactiveMacro.LeftClick(hwnd, self.combineBtn[0] + self.adjustCombineBtn[0], self.combineBtn[1] + self.adjustCombineBtn[1])
                            inactiveMacro.LRightClick(hwnd, self.jewelryBox[0] + self.adjustJewelryBox[0], self.jewelryBox[1] + self.adjustJewelryBox[1])
                            inactiveMacro.LeftClick(hwnd, self.combineBtn[0] + self.adjustCombineBtn[0], self.combineBtn[1] + self.adjustCombineBtn[1])
                            inactiveMacro.LeftClick(hwnd, self.cubeCorner[0] + self.adjustCubeCorner[0], self.cubeCorner[1] + self.adjustCubeCorner[1])
                            inactiveMacro.LeftClick(hwnd, self.jewelryBox[0] + self.adjustJewelryBox[0], self.jewelryBox[1] + self.adjustJewelryBox[1])
                            count = 0
        else:
            if not self.combineBtn:
                print('조합버튼을 찾기 못했습니다.')
            if not self.cube:
                print('큐브를 찾기 못했습니다.')
            if not self.jewelryBox:
                print('보석상자를 찾기 못했습니다.')

    def moveFindedJewelry2(self, jewelrysPos):

        flag = True
        if self.combineBtn and self.cube and self.jewelryBox:
            for jewelryPos in jewelrysPos:
                x, y = jewelryPos
                inactiveMacro.LRightClick(hwnd, x + int(x * self.__adjustMonitorSize[self.__monitorSize]), y + int(y * self.__adjustMonitorSize[self.__monitorSize]))
                if flag:
                    inactiveMacro.LRightClick(hwnd, self.jewelryBox[0] + self.adjustJewelryBox[0], self.jewelryBox[1] + self.adjustJewelryBox[1])
                    flag = False
                inactiveMacro.LeftClick(hwnd, self.combineBtn[0] + self.adjustCombineBtn[0], self.combineBtn[1] + self.adjustCombineBtn[1])
            inactiveMacro.LeftClick(hwnd, self.cubeCorner[0] + self.adjustCubeCorner[0], self.cubeCorner[1] + self.adjustCubeCorner[1])
            inactiveMacro.LeftClick(hwnd, self.jewelryBox[0] + self.adjustJewelryBox[0], self.jewelryBox[1] + self.adjustJewelryBox[1])
        else:
            if not self.combineBtn:
                print('조합버튼을 찾기 못했습니다.')
            if not self.cube:
                print('큐브를 찾기 못했습니다.')
            if not self.jewelryBox:
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
        hwnd = inactiveMacro.GetHandleName('D2Loader')
        g_l, g_t, g_w, g_h = inactiveMacro.GetWindowRect(hwnd)
        self.findEtc()
        self.findEtc2()
        self.SetPosThroughMonitor()
        jewelrysPos = self.findJewelryNum()
        self.moveFindedJewelry(jewelrysPos)

    def execute2(self):
        global g_l, g_t, g_w, g_h, hwnd

        hwnd = inactiveMacro.GetHandleName('D2Loader')
        g_l, g_t, g_w, g_h = inactiveMacro.GetWindowRect(hwnd)
        self.findEtc()
        self.findEtc2()
        self.SetPosThroughMonitor()
        jewelrysPos = self.findJewelryNum2()
        self.moveFindedJewelry2(jewelrysPos)

    def execute3(self):
        global g_l, g_t, g_w, g_h, hwnd

        try:
            hwnd = inactiveMacro.GetHandleName('D2Loader')
            g_l, g_t, g_w, g_h = inactiveMacro.GetWindowRect(hwnd)
            self.findEtc()
            self.findEtc2()
            self.SetPosThroughMonitor()
            jewelrysPos = self.findJewelryNum()
            jewelrysPos2 = self.findJewelryNum2()
            jewelrysPos3 = self.findJewelryNum3(jewelrysPos, jewelrysPos2)
            self.moveFindedJewelry(jewelrysPos)
            self.moveFindedJewelry2(jewelrysPos3)
        except:
            print('디아블로가 실행되어 있지 않습니다.')