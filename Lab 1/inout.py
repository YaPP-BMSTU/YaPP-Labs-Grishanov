class IO:
    def __init__(self, filepath):
        self.filepath = filepath

    def readfile(self):
        with open(self.filepath) as f:
            lines = f.readlines()
        f.close()
        return lines

    def printfile(self):
        lines = self.readfile()
        print(lines)

    @staticmethod
    def printTable(csv_table):
        count = 0
        for row in csv_table:
            if count == 1:
                print("|" + "=" * 113 + "|")
            print('| {:1} | {:^40} | {:^5} | {:^10} | {:^10} | {:^10} | {:^14} |'.format(*row))
            count += 1