from usecase import UseCase
from app import App


def main():
    print("Hi, please input filepath to .csv file")
    print("> ", end="")
    filepath = input()
    app = App(filepath)
    app.start()


if __name__ == "__main__":
    main()
