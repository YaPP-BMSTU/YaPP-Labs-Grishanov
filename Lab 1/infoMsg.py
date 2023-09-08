from entity import Entity


class InfoMessage(Entity):
    def __init__(self):
        super().__init__()
        self.infoMsg = None
        self.isInfo = False
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
