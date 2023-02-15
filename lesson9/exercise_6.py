# Sukurti 5 vardu lista ir print vardus lygus ir didesnius uz 5 simbolius


#List normal:

names = ["Oleg", "Petras", "Kestas", "Liudmila", "Ruslan"]

for name in names:
    if len(name) >=5:
        break
print(f'first:{names}')

#List comprehension:

names=[name for name in names if len(name)>=5]
print(f'second: {names}')

