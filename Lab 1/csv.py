from inout import IO
import customErrors


class CSV(IO):
    def __init__(self, filepath, csv_table=None):
        super().__init__(filepath)
        self.csvTable = csv_table

    def CreateCSVTable(self):
        csv_table = []
        for i in range(0, len(self.lines)):
            line_arr = self.lines[i].split(",")
            line_arr[-1] = line_arr[-1].replace("\n", "")
            if len(line_arr) != 7:
                raise customErrors.BrokeDemographicFileStruct
            if i == 0:
                self.header = line_arr
            if (self.region is not None and line_arr[1] == self.region) or self.region is None:
                csv_table.append(line_arr)
        self.csvTable = csv_table
        return csv_table
