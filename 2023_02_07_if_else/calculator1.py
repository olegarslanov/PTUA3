#  3. Write a small calculator application, that allows user to 
# enter two numbers and a operation, given and then do the 
# operation and print an answer.


print('Smart calculator app with limited functions')

#number_1
check = False

while check:
    number_1 = input('Please enter Your first number: ')
    try:
        number_1= float(number_1)
        check = True
    except ValueError:
        print('This is format is not valid!')

#number_2
check = False

while check:
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
