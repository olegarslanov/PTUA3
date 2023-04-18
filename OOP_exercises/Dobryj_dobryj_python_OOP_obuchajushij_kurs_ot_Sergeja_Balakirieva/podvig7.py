import sys


class StreamData:
    def __init__(self):
        self.FIELDS = None
        self.lst_in = None

    def create(self, fields, lst_values):
        self.FIELDS = fields
        self.lst_in = lst_values
        return len(self.FIELDS) == len(self.lst_in)


class StreamReader:
    FIELDS = ("id", "title", "pages")

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
