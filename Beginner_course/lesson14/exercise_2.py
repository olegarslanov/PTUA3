# Write a function that moves all elements of one type to the end of the list:

# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# Log out inputs and results in a file.

import logging


my_tuple = ([1, 3, 2, 4, 4, 1], 1)
my_list = list(my_tuple)

my_list_two = []
for element in my_list:
    if type(element) == list:
        my_list_two = element
    else:
        logging.warning("Not all elements are lists!")

print(my_list_two)

my_list_three = str(my_list_two)


def unique_values(str_list: list[str]) -> list[str]:
    new_str_list = []

    for value in str_list:
        if len(set(value))==len(value):
            new_str_list.append(value)

    return new_str_list

print("New string list:", unique_values(my_list_three))









# strings_list=["Oleg","Tatjana","Agata","Radomir","Milada"]


# def unique_values(str_list: list[str])->list[str]:
#     new_str_list=[]

#     for value in str_list:
#         if len(set(value))==len(value):
#             new_str_list.append(value)

#     return new_str_list

# print("New string list:", unique_values(strings_list))

















# def leave_list(list_one:tuple) -> list:
#     for element in list_one:
#         if type(element) != list:
#             list_three = del list_one[element]
#             print(list_three)
#         else:
#             # list_three = list_one
#             # print(list_one)
#             logging.warning('One element is not list!')
#     return list_three

# tuple_two = ([1,3,2,4,4,1], 1)
# list_two = list(tuple_two)


# result = leave_list(list_two)
# print(result)















# def move_to_end(list_one:list, integer_one:int) -> list:
#     list_one.append(integer_one)
#     return list_one
   
# list_two = [1,3,2,4,4,1]
# integer_two = 1

# result = move_to_end(list_two, integer_two)
# print(result)




# logging.debug(print_value(key = input('Please enter key value:')))

# if __name__ == "__main__":
#     number = input("Please enter number:")



# def money_collected(amount: float) -> None:
#     logging.info(f"Amount of money received {amount}")
#     if amount == 0:
#         sum = amount + 1
#         logging.warning("Exepted amount larger than 0")
#     #doing smth else
#     else:
#         sum = amount + 2
#     return sum

# print(money_collected(0))



# def money_collected(amount: float) -> float:
#     logging.info(f"Amount of money received {amount}")
#     if amount == 0:
#       logging.warning("Exepted amount, must be larger than 0")
#     #doing smth else

#     try:
#         # some code here
#         result = amount / amount
#         logging.debug(f'Result:{result}')
#         return result
    
#     except Exception as e:
#       logging.error(f'Error received: {e}')

# money_collected (0)



# def emergency_stop(is_stop_event: bool) -> None:
#    if is_stop_event:
#       logging.critical(f'Had to stop device due to unexpected stop event')
#       # func stop()

# emergency_stop(True)

# print(emergency_stop(True))



