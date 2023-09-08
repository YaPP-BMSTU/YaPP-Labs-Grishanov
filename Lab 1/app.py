from usecase import UseCase

art = """  ,---------------------------,
  |  /---------------------\  |
  | |                       | |
  | |     YaPP Lab1         | |
  | |      CSV Reader       | |
  | |       Grishanov       | |
  | |                       | |
  |  \_____________________/  |
  |___________________________|
,---\_____     []     _______/------,
/         /______________\           /|
/___________________________________ /  | ___
|                                   |   |    )
|  _ _ _                 [-------]  |   |   (
|  o o o                 [-------]  |  /    _)_
|__________________________________ |/     /  /
/-------------------------------------/|      ( )/
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select item menu:
0) Exit
1) Exec program
2) Set Region
3) Set Metrics Col
4) Clear Region & Metrics Col"""


class App(UseCase):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.point = None

    def start(self):
        self.checkFile()
        while 1:
            self.checkInfoMsg()
            self.clearInfo()
            self.clearError()
            print(art)
            while 1:
                try:
                    self.point = int(input("Choose menu point:\n> "))
                    break
                except:
                    print("Use correct symbols")
                    self.point = 0
            if self.point == 0:
                break
            elif self.point == 1:
                self.ReadFile()
                if self.checkError():
                    return
                self.CreateCSVTable()
                if self.checkError():
                    return
                self.PrintTable()
                if self.checkError():
                    return
                self.CalcColMetrics()
                if self.checkError():
                    return
                self.PrintMetrics()
                if self.checkError():
                    return
                self.CalcPercentileTable()
                if self.checkError():
                    return
                self.PrintPercentileTable()
                if self.checkError():
                    return
            elif self.point == 2:
                self.region = input("Set region:\n> ")
            elif self.point == 3:
                while 1:
                    try:
                        self.col = int(input("Set metrics col:\n> "))
                        self.col -= 1
                        break
                    except:
                        print("Choose correct metrics col!")
            elif self.point == 4:
                self.region = None
                self.col = None
