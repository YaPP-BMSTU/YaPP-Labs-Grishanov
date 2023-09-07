from inout import IO
from csv import Csv
from usecase import UseCase


def main():
    i = IO("for2lab.csv")
    data = i.readfile()
    csv = Csv(data)
    table = csv.CreateCSVTable()
    usecase = UseCase(table, data)
    print(usecase.calc_col_metrics(4))
    i.printTable(table)


if __name__ == "__main__":
    main()
