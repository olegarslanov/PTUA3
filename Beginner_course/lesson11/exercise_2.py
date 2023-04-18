# There's a great war between the even and odd numbers. Many numbers already lost 
# their lives in this war and it's your task to end this. You have to determine which
# group sums larger: the evens or the odds. The larger group wins.

# Create a function that takes a list of integers, sums the even and odd numbers
#  separately, then returns the difference between the sums of the even and odd numbers.

# Example:
# war_of_numbers([2, 8, 7, 5]) ➞ 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 is larger than 10
# So we return 12 - 10 = 2




war_of_numbers = ([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243])


lst = []
list_even=[]
list_odd=[]

def check_list_odd_even(lst):
  for x in war_of_numbers:
    lst.append(x)
  for number in lst:
    if number%2 == 0:
      list_even.append(number) 
    elif number%2 != 0:
      list_odd.append(number)   
    else:
      print("Something wrong!")
  print(sum(list_even) - sum(list_odd))
#   return list_even, list_odd

check_list_odd_even(lst)

