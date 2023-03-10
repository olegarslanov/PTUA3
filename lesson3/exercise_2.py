
# Write a python program that multiplies all items in the list
#  (all items are integers or floats in list, create a list yourself)

number1 = int(input("Please enter Your number1: "))
number2 = int(input("Please enter Your number2: "))
number3 = int(input("Please enter Your number3: "))

my_list = [number1, number2, number3]
x=1
for number in my_list:
   x= number * x 
print (x)