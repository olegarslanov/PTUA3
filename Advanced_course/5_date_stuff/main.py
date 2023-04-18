import datetime

# Tai butu: datetime.datetime.today() --> modulis.klase.metodas  !!!
x = datetime.datetime.today()
print(x)
# 2020-11-25 12:41:47.651313

x = datetime.date.today()
print(x)
# 2023-04-11

y = datetime.datetime(2020, 2, 29, 18, 20, 50)
print(y)
print(type(y))
# 2020-02-29 18:20:50
# <class 'datetime.datetime'>

print(y.strftime("%B/%Y/%d"))
print(type(y.strftime("%B/%Y/%d")))
# February/2020/29
# <class 'str'>


import datetime
import locale

# locale.setlocale(locale.LC_TIME, "lt_LT.UTF-8")
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))
# turetu buti lietuviskai


# Kaip prideti ar atimti laika

import datetime

now = datetime.datetime.now()
print(now)
print(now - datetime.timedelta(days=5))
print(now + datetime.timedelta(hours=5))
print(now + datetime.timedelta(days=20, hours=8))
# 2020-11-25 12:26:14.575023
# 2020-11-20 12:26:14.575023
# 2020-11-25 17:26:14.575023
# 2020-12-15 20:26:14.575023


import datetime

now = datetime.datetime.now()
nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
skirtumas = now - nepriklausomybes_diena
print(skirtumas.days)
# 10590

# Naudodami timedelta galime pamatuoti, per kiek laiko mūsų kompiuteris susidorojo su
#  užduotimi, pvz.:
# import datetime

# pradzia = datetime.datetime.today()
# for x in range(1000):
#     print("Labas")

# pabaiga = datetime.datetime.today()
# print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")
