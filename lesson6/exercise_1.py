# 1.Let user enter name, surname and age. Print if user is allowed
#   to enter an online casino or not. 21 is the age cap.

name=input('Please enter Your name:')
surname=input('Please enter Your surname:')
age=int(input('Please enter Your age:'))

if age >= 21:
    print(f'Your name is {name} and surname is {surname}. Your age is good. You can go to the casino')
else:
    print ('Go away little boy')




