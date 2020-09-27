"""
    작성일 : 20/09/27
"""

import pyautogui
import time
import win32gui

jewelrys = ['diamond', 'amethyst', 'emerald', 'ruby', 'sapphire', 'skull', 'topaz']
confidences = [0.95, 0.95, 0.9, 0.95, 0.95, 0.95, 0.95]
g_l, g_t, g_w, g_h = 0, 0, 0, 0

""" 
    보석 개수 찾기
    로직 : 개수가 3개 이상일 경우 짝을 지어 묶어 반환
    @return 각 보석 위치
"""

def findJewelryNum():

    jewelrysPos = []

    for i, jewelry in enumerate(jewelrys):
        
        data = list(pyautogui.locateAllOnScreen('img/jewelry/' + jewelry + '.PNG', confidence = confidences[i], region = (g_l, g_t, g_w, g_h)))
        jewelrysPos.append([])

        if len(data) > 2:
            print(jewelry, str(len(data)) + '개', '찾음')
            for j in range(3 * (len(data) // 3)):
                x, y = pyautogui.center(data[j])
                jewelrysPos[i].append([x,y])
        else:
            print(jewelry, str(3 - len(data)) + '개', '부족')

    return jewelrysPos
    
def findJewelryNum2():

    jewelrysPos = []

    for i, jewelry in enumerate(jewelrys):
        
        jewelrysPos.extend(list(pyautogui.locateAllOnScreen('img/jewelry/' + jewelry + '.PNG', confidence = confidences[i], region = (g_l, g_t, g_w, g_h))))

    return jewelrysPos

def findJewelryNum3(jewelrysPos, jewelrysPos2):

    tmp = []

    for i in jewelrysPos:
        for j in i:
            tmp.append(j)

    jewelrysPos2 = list(map(lambda x : list(pyautogui.center(x)), jewelrysPos2))

    for i in range(len(jewelrysPos2)-1, -1, -1):
        if jewelrysPos2[i] in tmp:
            del jewelrysPos2[i]

    return jewelrysPos2

"""
    큐브와 조합버튼 찾기
    @return 큐브, 조합버튼 위치
"""
def findEtc():

    combineBtn = pyautogui.locateCenterOnScreen('img/function/combine.PNG', confidence = 0.9, region = (g_l, g_t, g_w, g_h))
    cube = pyautogui.locateCenterOnScreen('img/boxs/cube.PNG', confidence = 0.9, region = (g_l, g_t, g_w, g_h))
    jewelryBox = pyautogui.locateCenterOnScreen('img/boxs/jewelryBox.PNG', confidence = 0.9, region = (g_l, g_t, g_w, g_h))
    cubeCorner = pyautogui.locateCenterOnScreen('img/etc/cubeCorner.PNG', confidence = 0.9, region = (g_l, g_t, g_w, g_h))

    return combineBtn, cube, jewelryBox, cubeCorner

""" 
    sleep을 조합한 클릭
"""
def improvedClick(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(.1)

"""
    쥬얼 합성
"""
def moveFindedJewelry(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner):

    if combineBtn and cube and jewelryBox:
        for jewelryPos in jewelrysPos:
            if jewelryPos:
                count = 0
                for x, y in jewelryPos:
                    improvedClick(x, y)
                    improvedClick(cube[0], cube[1])
                    count += 1
                    if count == 3:
                        improvedClick(combineBtn[0], combineBtn[1])
                        improvedClick(jewelryBox[0], jewelryBox[1])
                        improvedClick(cube[0], cube[1])
                        improvedClick(combineBtn[0], combineBtn[1])
                        improvedClick(cubeCorner[0], cubeCorner[1])
                        improvedClick(jewelryBox[0], jewelryBox[1])
                        count = 0
    else:
        if not combineBtn:
            print('조합버튼을 찾기 못했습니다.')
        if not cube:
            print('큐브를 찾기 못했습니다.')
        if not jewelryBox:
            print('보석상자를 찾기 못했습니다.')

def moveFindedJewelry2(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner):

    if combineBtn and cube and jewelryBox:
        for jewelryPos in jewelrysPos:
            x, y = pyautogui.center(jewelryPos)
            improvedClick(x, y)
            improvedClick(cube[0], cube[1])
            improvedClick(jewelryBox[0], jewelryBox[1])
            improvedClick(cube[0], cube[1])
            improvedClick(combineBtn[0], combineBtn[1])
            improvedClick(cubeCorner[0], cubeCorner[1])
            improvedClick(jewelryBox[0], jewelryBox[1])
    else:
        if not combineBtn:
            print('조합버튼을 찾기 못했습니다.')
        if not cube:
            print('큐브를 찾기 못했습니다.')
        if not jewelryBox:
            print('보석상자를 찾기 못했습니다.')

def moveFindedJewelry3(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner):

    if combineBtn and cube and jewelryBox:
        for jewelryPos in jewelrysPos:
            x, y = jewelryPos
            improvedClick(x, y)
            improvedClick(cube[0], cube[1])
            improvedClick(jewelryBox[0], jewelryBox[1])
            improvedClick(cube[0], cube[1])
            improvedClick(combineBtn[0], combineBtn[1])
            improvedClick(cubeCorner[0], cubeCorner[1])
            improvedClick(jewelryBox[0], jewelryBox[1])
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
def jewelryCombineMain():

    global g_l, g_t, g_w, g_h

    try:
        hwnd = win32gui.FindWindow('Diablo II',None)
        g_l, g_t, g_w, g_h = win32gui.GetWindowRect(hwnd)
        combineBtn, cube, jewelryBox, cubeCorner = findEtc()
        g_l += (g_w - g_l) // 2
        g_t += (g_h - g_t) // 2
        jewelrysPos = findJewelryNum()
        moveFindedJewelry(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner)
    except:
        print('디아블로가 실행되어 있지 않습니다.')

def jewelryCombineMain2():

    global g_l, g_t, g_w, g_h

    try:
        hwnd = win32gui.FindWindow('Diablo II',None)
        g_l, g_t, g_w, g_h = win32gui.GetWindowRect(hwnd)
        combineBtn, cube, jewelryBox, cubeCorner = findEtc()
        g_l += (g_w - g_l) // 2
        g_t += (g_h - g_t) // 2
        jewelrysPos = findJewelryNum2()
        moveFindedJewelry2(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner)
    except:
        print('디아블로가 실행되어 있지 않습니다.')

def jewelryCombineMain3():

    global g_l, g_t, g_w, g_h

    try:
        hwnd = win32gui.FindWindow('Diablo II',None)
        g_l, g_t, g_w, g_h = win32gui.GetWindowRect(hwnd)
        combineBtn, cube, jewelryBox, cubeCorner = findEtc()
        g_l += (g_w - g_l) // 2
        g_t += (g_h - g_t) // 2
        jewelrysPos = findJewelryNum()
        jewelrysPos2 = findJewelryNum2()
        jewelrysPos3 = findJewelryNum3(jewelrysPos, jewelrysPos2)
        moveFindedJewelry(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner)
        moveFindedJewelry3(jewelrysPos3, combineBtn, cube, jewelryBox, cubeCorner)
    except:
        print('디아블로가 실행되어 있지 않습니다.')