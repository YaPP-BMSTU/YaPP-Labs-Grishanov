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
            temp = ""
            for i in range(2, 7):
                try:
                    float(line_arr[i])
                except:
                    raise customErrors.BrokeDemographicFileStruct
            for k in line_arr:
                temp += k
            if temp == "":
                continue
            if len(line_arr) != 7:
                raise customErrors.BrokeDemographicFileStruct
            if i == 0:
                self.header = line_arr
                if line_arr[0] != "year" or line_arr[1] != "region" or line_arr[2] != "npg" or line_arr[3] != "birth_rate" or line_arr[4] != "death_rate" or line_arr[5] != "gdw" or line_arr[6] != "urbanization":
                    raise customErrors.IncorrectHeader
            if ((self.region is not None and line_arr[1] == self.region) or self.region is None) and i != 0:
                csv_table.append(line_arr)
        self.csvTable = csv_table
        return csv_table
