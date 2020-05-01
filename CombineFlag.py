import time

class CombineFlag:

    def __init__(self):

        self.flag = True
        self.time = time.time()
        self.timeGrade = 0

    def initTime(self):

        self.time = time.time()

    def initTimeGrade(self):

        self.timeGrade = 0

    def getFlag(self):

        return self.flag

    def getTime(self):

        return time.time() - self.time

    def getTimeGrade(self):

        return self.timeGrade

    def setFlag(self, judge):

        self.flag = judge

    def plusTimeGrade(self):

        self.timeGrade += 1
