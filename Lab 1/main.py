from app import App


def main():
    while 1:
        print("Hi, please input filepath to .csv file")
        print("> ", end="")
        filepath = input()
        app = App(filepath)
        try:
            app.checkFile()
            break
        except Exception as err:
            print(err)
    app.start()


if __name__ == "__main__":
    main()
