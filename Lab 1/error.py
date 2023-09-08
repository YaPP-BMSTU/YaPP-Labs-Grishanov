class Error:
    def __init__(self):
        self.isError = False
        self.isInfo = False
        self.infoMsg = None
        self.error = None
        self.levelError = None

    def setInfoMsg(self, info):
        self.isInfo = True
        self.infoMsg = info

    def clearInfo(self):
        self.isInfo = False
        self.infoMsg = ""

    def checkInfoMsg(self):
        if self.isInfo:
            print(self.infoMsg)
        return self.isInfo

    def setError(self, error, levelError):
        self.isError = True
        self.error = error
        self.levelError = levelError

    def clearError(self):
        self.isError = False
        self.error = ""
        self.levelError = ""

    def checkError(self):
        if self.isError:
            print(self.error, self.levelError)
        return self.isError
