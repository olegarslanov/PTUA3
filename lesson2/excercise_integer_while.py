# How to enter right data for matematical operations

print ('a * b =')

first_check = False
while first_check is False:
    a = input('a= ')
    try:
        a = int(a)
        first_check = True
    except ValueError:
            print('You must enter an integer')


second_check = False
while second_check is False:
    b = input('b= ')
    try:
        b = int(b)
        second_check = True
    except ValueError:
            print('You must enter an integer')


print('Answer is: ', a*b)

