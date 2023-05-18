import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    def insert(self, data):
        self.data = data

    def select(self, a, b):
        return self.lst_data[a : b + 1]
