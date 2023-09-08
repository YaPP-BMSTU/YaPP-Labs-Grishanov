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
4) Set New Filepath
5) Clear Region & Metrics Col"""


class App(UseCase):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.point = None

    def start(self):
        self.checkFile()
        while 1:
            self.checkInfoMsg()
            self.clearInfo()
            print(art)
            while 1:
                try:
                    self.point = int(input("Choose menu point:\n> "))
                    break
                except Exception as err:
                    print(err)
                    print("Use correct symbols")
                    self.point = 0
            if self.point == 0:
                break
            else:
                self.menu()

    def menu(self):
        if self.point == 1:
            self.exec()
        elif self.point == 2:
            self.region = input("Set region:\n> ")
        elif self.point == 3:
            while 1:
                try:
                    self.col = int(input("Set metrics col:\n> "))
                    self.col -= 1
                    break
                except Exception as err:
                    print(err)
                    print("Choose correct metrics col!")
        elif self.point == 4:
            while 1:
                try:
                    self.filepath = input("Set new filepath:\n> ")
                    self.checkFile()
                    break
                except Exception as err:
                    print(err)
                    print("Choose correct file!")
        elif self.point == 5:
            self.region = None
            self.col = None

    def exec(self):
        self.ReadFile()
        self.CreateCSVTable()
        self.PrintTable()
        self.CalcColMetrics()
        self.PrintMetrics()
        self.CalcPercentileTable()
        self.PrintPercentileTable()