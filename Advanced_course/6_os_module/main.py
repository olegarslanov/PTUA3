import os

# os.chdir("C:/Users/olega/projects/Codeacademy/Python_lessons/")
# print(os.getcwd())

# print(os.listdir())

# os.mkdir("new_folder")

# os.makedirs("New_folder2/something")

# print(os.stat("main.py"))

# from datetime import datetime
# data = os.stat("naujas_tekstas.txt").st_mtime
# print(datetime.fromtimestamp(data))

# 2019-03-20 11:09:25.198372

# Tekstinių failų kūrimas ir nuskaitymas

# with open("file.txt", "a") as f:
#     f.write("Hello World 123")


# f = open("file.txt", 'a')
# f.write("Sveikas, pasauli!")
# f.close()


with open("failas.txt", "r") as failas:
    print(failas.read())
    failas.write("Labas rytas, pasauli!")

# Sveikas, pasauli!

with open("failas.txt", "r") as failas:
    print(failas.read())

# Sveikas, pasauli!Labas rytas, pasauli!

#       Kad padaryti kopija paveiksliuko:
# with open("logo.png", "rb") as r_failas:
#     with open("logo_kopija.png", "wb") as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)


import pickle
