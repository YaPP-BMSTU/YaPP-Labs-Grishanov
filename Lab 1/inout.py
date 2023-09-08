import os.path

from error import Error

MAX_FILESIZE = 1.28e+8


class IO(Error):
    def __init__(self, filepath):
        super().__init__()
        self.lines = None
        self.filepath = filepath
        self.csvTable = None
        self.header = None
        self.region = None
        self.minValue = None
        self.maxValue = None
        self.mediumValue = 0
        self.medianValue = 0
        self.percentileTable = [0 for k in range(0, 20)]

    def checkFile(self):
        if not os.path.exists(self.filepath):
            self.setError("Filepath is wrong!", "In/Out")
            return
        if os.path.getsize(self.filepath) > MAX_FILESIZE:
            self.setError("Your File is too big!", "In/Out")
            return
        if os.path.getsize(self.filepath) == 0:
            self.setError("Your file is empty!", "In/Out")
            return

    def ReadFile(self):
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
