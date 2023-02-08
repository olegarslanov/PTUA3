# count in what year user born


import datetime
x= datetime.datetime.now()
current_year = x.year

age = int(input ('Please enter Your age:'))


clause = input('Did You already have s birthday this year (Y/N)?')

if clause == 'Y':
    birth_year = current_year - age
else:
    birth_year = current_year - age - 1



print (birth_year)