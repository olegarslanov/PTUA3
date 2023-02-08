# # 1.Let user enter name, surname and age. Print if user is allowed
# #   to enter an online casino or not. 21 is the age cap.

#  name=input('Please enter Your name:')
#  surname=input('Please enter Your surname:')
#  age=int(input('Please enter Your age:'))

#  if age >= 21:
#      print(f'Your name is {name} and surname is {surname}. Your age is good. You can go to the casino')
#  else:
#      print ('Go away little boy')



# # 2. Create a database (List of privileged users) print a specific
# #   message with a personal greeting if the user is a privileged 
# #  and just "Welcome otherwise"

#  programmer=input('Please enter Your name:')
#  privileged_programmers = ["Oleg", "Tomas", "Remigijus"]
#  if programmer in privileged_programmers:
#      print(f"{programmer} You are best python programmer")
#  else:
#      print("INTRUDER ALLERT. Silently calling police...")




#3. allow user to enter two numbers, print out which one is higher 
#   than the other, or are they equal?


# number_1 =int(input('Please enter Your number_1:'))
# number2 =int(input('Please enter Your second number2:'))

# if number_1 > number2:
#     print('_ is greater')
# elif number_1 == number2:
#     print('numbers are equals')
# else: 
#     print('number2 is greater')

# #2
# numbers=input('Please enter two integer numbers(example: 1,2):').split(',')

# print(numbers)

# number_1=int(numbers[0])
# number_2=int(numbers[1])

# if number_1 > number_2:
#     print(f'number 1: {number_1} < number 2: {number_2}')
# elif number_1 < number_2:
#     print(f'number 1: {number_1} < number 2: {number_2}')
# else:
#     print(f'number 1: {number_1} = number 2: {number_2}')



# 3. Write a small calculator application, that allows user to 
# enter two numbers and a operation, given and then do the 
# operation and print an answer.


print('Smart calculator app with limited functions')

#number_1
check = False

while check is False:
    number_1 = input('Please enter Your first number: ')
    try:
        number_1= float(number_1)
        check = True
    except ValueError:
        print('This is format is not valid!')

#number_2
check = False

while check is False:
    number_2 = input('Please enter Your second number: ')
    try:
        number_2= float(number_2)
        check = True
    except ValueError:
        print('This is format is not valid!')

#operation
operations=['*','/','+','-']

check = False

while not check:
    operation = input('Please enter matematical operation(+,-,/,*):')
    if operation in operations:
        check=True
    

#count       

if operation == '+':
    answer = number_1+number_2
elif operation =='-':
     answer=number_1-number_2
elif operation =='*':
    answer=number_1*number_2
elif operation =='/':
    answer=number_1/number_2

print('Answer=', round(answer,2))

