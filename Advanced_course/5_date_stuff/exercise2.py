# Parašyti programą, kuri:

# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

# https://www.w3schools.com/python/python_datetime.asp

import datetime

y = datetime.datetime.today()
print(y)

now = datetime.datetime.now()
print(now - datetime.timedelta(days=5))

now = datetime.datetime.now()
print(now - datetime.timedelta(hours=5))

y = datetime.datetime.today()
print(y.strftime("%Y %m %d, %X"))
