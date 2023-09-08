from csv import CSV
import customErrors


class UseCase(CSV):
    def __init__(self, filepath, region=None, col=None):
        super().__init__(filepath)
        self.maxValue = None
        self.minValue = None
        self.medianValue = None
        self.colArr = None
        self.col = col
        self.region = region

    def __GetColArray(self):
        if self.col < 2 or self.col > 6:
            raise customErrors.WrongSelectedColumn
        arr = []
        for i in range(1, len(self.csvTable)):
            try:
                arr.append(float(self.csvTable[i][self.col]))
            except:
                pass
        arr.sort()
        self.colArr = arr
        return arr

    def CalcColMetrics(self):
        if self.col is not None:
            self.__GetColArray()
            self.minValue = self.colArr[0]
            self.maxValue = self.colArr[-1]
            if len(self.colArr) % 2 == 0:
                self.medianValue += self.colArr[len(self.colArr) // 2]
                self.medianValue += self.colArr[len(self.colArr) // 2 - 1]
                self.medianValue /= 2
            else:
                self.medianValue = self.colArr[len(self.colArr) // 2]
            for elem in self.colArr:
                self.mediumValue += elem
            self.mediumValue /= len(self.colArr)
        else:
            self.setInfoMsg("Col is not selected!")

    def CalcPercentileTable(self):
        if self.colArr is not None:
            indexArr = 0
            for percent in range(0, 100, 5):
                percentileIndex = round((percent / 100) * (len(self.colArr) - 1))
                self.percentileTable[indexArr] = self.colArr[percentileIndex]
                indexArr += 1
        else:
            self.setInfoMsg("Current array col is empty!")
