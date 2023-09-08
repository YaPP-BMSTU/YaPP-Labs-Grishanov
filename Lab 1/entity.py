class Entity:
    def __init__(self):
        self.lines = None
        self.csvTable = None
        self.header = None
        self.region = None
        self.minValue = None
        self.maxValue = None
        self.mediumValue = 0
        self.medianValue = 0
        self.percentileTable = [0 for k in range(0, 20)]