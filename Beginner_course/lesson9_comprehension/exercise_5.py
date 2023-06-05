# Write a program that checks if given number is a perfect square.


#1
input_a = int(input('Please input number:'))


list=[]
for value in range(0,input_a):
    list.append(value**2)

for value in list:
    if value==input_a:
        print("You entered  perfect square number")

print("It is not perfect square")


#2
input_a = int(input('Please input number:'))


list=[]
for value in range(0,input_a):
    list.append(value**2)
    if value==input_a:
        print("You entered  perfect square number")


print("It is not perfect square")


#comprehension



