# 4. Write a small calculator application, that allows user to 
# enter two numbers and a operation, given and then do the 
# operation and print an answer.

print('Smart calculator app with limited functions')

number_1 = float(input('Please enter Your first number: '))
number_2 = float(input('Please enter Your second number: '))
sign = input('Please enter matematical operation(+,-,/,*):')

signs=['*','/','+','-']

if sign == "+":
   answer=number_1+number_2
elif sign == "-":
    answer=number_1-number_2
elif sign =="*":
    answer=number_1*number_2
elif sign =="/":
    answer=number_1/number_2
else:
    print("This function is not compactible!")

print("Answer is",answer)





