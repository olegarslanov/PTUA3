
# 3. allow user to enter two numbers, print out which one is higher 
#   than the other, or are they equal?


number_1 =int(input('Please enter Your number_1:'))
number_2 =int(input('Please enter Your second number2:'))


if number_1 > number_2:
    print('number1 is greater')
elif number_1 == number_2:
    print('numbers are equals')
else: 
    print('number2 is greater')

#2
numbers=input('Please enter two integer numbers(example: 1,2):').split(',')

print(numbers)

number_1=int(numbers[0])
number_2=int(numbers[1])

if number_1 > number_2:
    print(f'number 1: {number_1} < number 2: {number_2}')
elif number_1 < number_2:
    print(f'number 1: {number_1} < number 2: {number_2}')
else:
    print(f'number 1: {number_1} = number 2: {number_2}')




