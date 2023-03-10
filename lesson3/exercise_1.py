# Write a python program that sums up all items in the list 
# (all items are integers or floats in list, create a list yourself)

number1 = int(input("Please enter Your number1: "))
number2 = int(input("Please enter Your number2: "))
number3 = int(input("Please enter Your number3: "))

my_list = [number1, number2, number3]

print(sum(my_list))



def sum_of_list(l,n):
  if n == 0:
    return l[n];
  return l[n] + sum_of_list(l,n-1)

my_list = [1,3,5,2,4]
print ("The sum of my_list is", sum_of_list(my_list,len(my_list)-1))



def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [1,3,5,2,4]
print ("The sum of my_list is", sum_of_list(my_list))





