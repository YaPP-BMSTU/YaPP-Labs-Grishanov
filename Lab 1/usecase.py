from csv import Csv


class UseCase(Csv):
    def __init__(self, csv_table, lines):
        super().__init__(lines, csv_table)
        self.col_arr = None
        self.col = None

    def get_col_array(self, col):
        arr = []
        for i in range(1, len(self.csv_table)):
            try:
                arr.append(float(self.csv_table[i][col]))
            except:
                pass
        arr.sort()
        self.col_arr = arr
        self.col = col
        return arr

    def calc_col_metrics(self, col):
        if col != self.col:
            self.get_col_array(col)
        min_value = self.col_arr[0]
        max_value = self.col_arr[-1]
        medium_value = 0
        if len(self.col_arr) % 2 == 0:
            medium_value += self.col_arr[len(self.col_arr) // 2]
            medium_value += self.col_arr[len(self.col_arr) // 2 - 1]
            medium_value /= 2
        else:
            medium_value = self.col_arr[len(self.col_arr) // 2]
        return min_value, max_value, medium_value
