# Objavite klass s imenem MediaPlayer s dvumia metodami:
# open(file) - dlia otkrytija media faila s imenem file (sozdajet lokalnoje svoistvo
# filename so znachenijem argumenta file  objekte MediaPlayer)
# play() - dlja vosproizvedenija media faila (vyvodit na ekran stroku
# "Vosproizvedenije <nazvanije media faila>"

# Sozdaite dva egzempliara etogo klassa s imenami: media1 i media2. Vyzovite iz
# nih metod open() s argumentom "filemedia1" dlja objekta media1 i "filemedia2"
# dlja objekta media2. Posle etogo vyzovite cherez objekty metod play().
# Pri etom na ekrane dolzhno otobrazitsja dve strochki (bez kavychek):
# "Vosproizvedenije filemedia1"
# "Vosproizvedenije filemedia2"


class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Vosproizvedenije {self.filename}")


media1 = MediaPlayer()
media1.open("filemedia1")
media1.play()

media2 = MediaPlayer()
media2.open("filemedia2")
media2.play()


# class MediaPlayer:
#     def open(self, file):
#         self.file = file

#     def play(self):
#         print(f"Vosproizvedenije {self.file}")


# media1 = MediaPlayer()
# media1.open("filemedia1")
# media1.play()

# media2 = MediaPlayer()
# media2.open("filemedia2")
# media2.play()
