print (5>10)
if 5>=10:
    print('YES')

print('finishing program')



number1 = int(input('Enter your age:'))
number2 = 600
if number1 < number2:
    print("number1 is greater than number2 !")
elif number1 == number2:
    print("numbers are equal !")
else:
    print("number2 is greater than number1 !")



if len('apple') <len('apple'):
    print('it exists!')


a = 200
b = 450
print("A") if a > b else print("B")



a = 200
b = 400
c = 500
if c > a and c > b:
    print("C is the greatest of them all!")


a = 200
b = 400
c = 500
if b > a or b > c:
    print("B is at least greater than one of the values !")
if c > a and c > b:
    print("C is the greatest of them all!")    



# Nested if

x = 15

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#pass

a = 50
b = 80

if b > a:
  pass

