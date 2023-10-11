class WrongFilepath(Exception):
    def __init__(self, message="Wrong filepath!"):
        self.message = message
        super().__init__(self.message)


class FileTooBig(Exception):
    def __init__(self, message="File too big!"):
        self.message = message
        super().__init__(self.message)


class EmptyFile(Exception):
    def __init__(self, message="File is empty!"):
        self.message = message
        super().__init__(self.message)


class WrongSelectedColumn(Exception):
    def __init__(self, message="Current column is wrong! Can't calculate!"):
        self.message = message
        super().__init__(self.message)


class BrokeDemographicFileStruct(Exception):
    def __init__(self, message="Current file is broken! Struct not correct!"):
        self.message = message
        super().__init__(self.message)


class WrongFileExtension(Exception):
    def __init__(self, message="Wrong file extension! Use only .csv file"):
        self.message = message
        super().__init__(self.message)


class IncorrectHeader(Exception):
    def __init__(self, message="Incorrect header in .csv file"):
        self.message = message
        super().__init__(self.message)
