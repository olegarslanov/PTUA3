# Allow user to enter 10 integers, and then print the sum 
# and average of those entered numbers.

# enter only integer

# first_check = False
# print('print1')
# while first_check is False:
#     print('print2')
#     integer_1 = input('Please enter first integer:')
#     print('print3')
#     try:
#         print('print4')
#         integer_1 = int(integer_1)
#         print('print5')
#         first_check = True
#         print('print6')
#     except ValueError:
#         print('You must enter an integer:')
    
# print(integer_1)




while True:
    user_input = input("Enter your integer: ")
    if user_input == int(user_input):
        user_input=int(user_input)
        break
    else:
        print('Please enter only integer!')


print(f"You entered {user_input }")





# if int('15')==15:
#     print ('ha ha')
# else:
#     print('pisec')