class Sakinys:
    def text_atbulai(self, txt):
        self.txt = txt[::-1]
        return self.txt


sakinys = Sakinys()
print(sakinys.text_atbulai("abrakadabra"))
