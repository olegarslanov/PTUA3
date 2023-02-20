# Write a function that takes two lists and adds the first element in the first list 
# with the first element in the second list, the second element in the first list with
#  the second element in the second list, etc, etc. Return True if all element 
# combinations add up to the same number. Otherwise, return False. 
# Example: puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# Both lists sum to [5, 5, 5, 5]


lists=([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6])

list_value_sum=[sum(x) for x in zip(*lists)]
# print(list_value_sum)

# check list values if they same -> True, else -> False 

def any_one(iterable):
  it=iter








# def list_element_add_check (a,b):
#     for





# def adding(list_1[i],list_2[i]):
#     for all in puzzle_pieces:
#         list_1[0]+list_2[0]









# def find_sum(num1,num2):
#     """Return the sum of num1 and num2"""
#     sum=num1+mum2
#     return sum


# def my_function(f_name):
#   print(f_name + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")







