"""
    작성일 : 20/09/27
"""

import pyautogui
import time

jewelrys = ['diamond', 'amethyst', 'emerald', 'ruby', 'sapphire', 'skull', 'topaz']
confidences = [0.99, 0.99, 0.9, 0.99, 0.99, 0.99, 0.99]

""" 
    보석 개수 찾기
    로직 : 개수가 3개 이상일 경우 짝을 지어 묶어 반환
    @return 각 보석 위치
"""
def findJewelryNum():

    jewelrysPos = []

    for i, jewelry in enumerate(jewelrys):
        
        data = list(pyautogui.locateAllOnScreen('img/jewelry/' + jewelry + '.PNG', confidence = confidences[i]))
        jewelrysPos.append([])

        if len(data) > 2:
            print(jewelry, str(len(data)) + '개', '찾음')
            for j in range(3 * (len(data) // 3)):
                x, y = pyautogui.center(data[j])
                jewelrysPos[i].append([x,y])
        else:
            print(jewelry, '못찾음')

    return jewelrysPos

"""
    큐브와 조합버튼 찾기
    @return 큐브, 조합버튼 위치
"""
def findEtc():

    combineBtn = pyautogui.locateCenterOnScreen('img/function/combine.PNG', confidence = 0.99)
    cube = pyautogui.locateCenterOnScreen('img/boxs/cube.PNG', confidence = 0.99)
    jewelryBox = pyautogui.locateCenterOnScreen('img/boxs/jewelryBox.PNG', confidence = 0.99)
    cubeCorner = pyautogui.locateCenterOnScreen('img/etc/cubeCorner.PNG', confidence = 0.99)

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
                for x, y in jewelryPos:
                    improvedClick(x, y)
                    improvedClick(cube[0], cube[1])
                improvedClick(combineBtn[0], combineBtn[1])
                improvedClick(jewelryBox[0], jewelryBox[1])
                improvedClick(cube[0], cube[1])
                improvedClick(combineBtn[0], combineBtn[1])
                improvedClick(cubeCorner[0], cubeCorner[1])
                improvedClick(jewelryBox[0], jewelryBox[1])
                break 
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
    
    jewelrysPos = findJewelryNum()
    combineBtn, cube, jewelryBox, cubeCorner = findEtc()
    moveFindedJewelry(jewelrysPos, combineBtn, cube, jewelryBox, cubeCorner)




