import os.path

from infoMsg import InfoMessage
import customErrors

MAX_FILESIZE = 1.28e+8


class IO(InfoMessage):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

    def checkFile(self):
        if not os.path.exists(self.filepath):
            raise customErrors.WrongFilepath()
        if self.filepath[len(self.filepath)-4:len(self.filepath)] != ".csv":
            raise customErrors.WrongFileExtension
        if os.path.getsize(self.filepath) > MAX_FILESIZE:
            raise customErrors.FileTooBig()
        if os.path.getsize(self.filepath) == 0:
            raise customErrors.EmptyFile()

    def ReadFile(self):
        self.checkFile()
        with open(self.filepath) as f:
            lines = f.readlines()
        f.close()
        self.lines = lines
        return lines

    def PrintTable(self):
        print('| {:1} | {:^40} | {:^5} | {:^10} | {:^10} | {:^10} | {:^14} |'.format(*self.header))
        print("|" + "=" * 113 + "|")
        for row in self.csvTable:
            print('| {:1} | {:^40} | {:^5} | {:^10} | {:^10} | {:^10} | {:^14} |'.format(*row))

    def PrintMetrics(self):
        if self.minValue is not None and self.maxValue is not None:
            print("Metrics:")
            print('| {:^20} | {:^20} | {:^20} | {:^20} |'.format("Min", "Max", "Medium", "Median"))
            print('| {:^20} | {:^20} | {:^20} | {:^20} |'.format(str(self.minValue), str(self.maxValue), str(self.mediumValue), str(self.medianValue)))

    def PrintPercentileTable(self):
        if self.minValue is not None and self.maxValue is not None:
            print("Percentile Table:")
            for i in range(0, len(self.percentileTable)):
                print('| {:^5} | {:^8} |'.format(i * 5, self.percentileTable[i]))
