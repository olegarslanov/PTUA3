import sys

class StreamData:
    def create(self, fields, lst_values):
        


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.redLines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
    
sr = StreamReader()
data, result = sr.readLines()

