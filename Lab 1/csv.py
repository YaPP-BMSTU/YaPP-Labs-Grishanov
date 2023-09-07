class Csv:
    def __init__(self, lines, csv_table=None):
        self.csv_table = csv_table
        self.lines = lines
        self.length = len(lines)

    def CheckRecords(self):
        # Records
        pass

    def GetHeader(self):
        return self.lines[0]

    def GetAllRecords(self):
        return self.lines[1:self.length].replace("\n", "")

    def CreateCSVTable(self):
        csv_table = []
        for line in self.lines:
            line_arr = line.split(",")
            line_arr[-1] = line_arr[-1].replace("\n", "")
            csv_table.append(line_arr)
        self.csv_table = csv_table
        return csv_table

