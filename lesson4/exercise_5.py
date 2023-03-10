
# Write a program that allows user to write in any float 
# number and then round it.



print('Task for filter only floats ant round them')

check = False
while check is False:
    user_input = input('Please enter float: ')
    try:
        user_input= float(user_input)
        check = True
    except ValueError:
        print('This is not float!')

print('Atsakymas:', round(user_input,2))


