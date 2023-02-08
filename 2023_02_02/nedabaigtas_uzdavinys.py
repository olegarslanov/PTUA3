# 5. write a program that allows user to write in any float 
# # number and then round it.


# print('Task for filter only floats ant round them')

# check = False

# while check is False:
#     user_input = input('Please enter float: ')
#     try:
#         user_input= float(user_input)
#         check = True
#     except ValueError:
#         print('This is not float!')

# print('Atsakymas:', round(user_input,2))



# # user_input=input('Iveskite skaiciu')

# if user_input == int(user_input):
#     print('This is not float!')
# else:
#     user_input=input('Please enter float:')


operation_list=['*','/','+','-']

# check = False

# while check is False:
#     operation = input('Please enter matematical operation(+,-,/,*):')
#     try:
        
#     except ValueError:
#         print('This is format is not valid!')

operation = input('Please enter matematical operation(+,-,/,*):')
for operation in operation_list:
    check=True

print(check)