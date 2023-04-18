# Write a function that takes two lists and adds the first element in the first list 
# with the first element in the second list, the second element in the first list with
#  the second element in the second list, etc, etc. Return True if all element 
# combinations add up to the same number. Otherwise, return False. 
# Example: puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# Both lists sum to [5, 5, 5, 5]



lists=([1,2,3,4], [4,3,2,1])

# list_value_sum=[sum(x) for x in zip(*lists)]

# print(list_value_sum)


# check list values if they same -> True, else -> False 

# if len(set(list_value_sum))!=len(list_value_sum):
#   print ("True")
# else:
#   print("False")




def check_list_same_numbers(lists):
  list_value_sum=[sum(x) for x in zip(*lists)]
  if len(set(list_value_sum))!=len(list_value_sum):
    print ("True")
  else:
    print("False")

check_list_same_numbers(lists)




