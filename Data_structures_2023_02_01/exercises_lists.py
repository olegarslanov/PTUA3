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




# # Write a python program that multiplies all items in the list
# #  (all items are integers or floats in list, create a list yourself)

number1 = int(input("Please enter Your number1: "))
number2 = int(input("Please enter Your number2: "))
number3 = int(input("Please enter Your number3: "))

my_list = [number1, number2, number3]
x=1
for number in my_list:
   x= number * x 
print (x)

# # # Write a python program that gets maximum value from the list
# # #  (all items are integers or floats in list, create a list yourself)

my_list = [1,2,3,4,5]
print("Didziausia reiksme: ", max(my_list))


# # # Write a python program that concatenates all strings in the list
# # #  (all items are strings, create a list yourself)

my_list = ["Oleg", "is good", "programmer"]
for item in my_list:
    print(item)


# Create two lists and add them together, make sure it works the way you want it to.

my_list1 = [1,2,3]
my_list2 = [4,5,6]
res= my_list1+my_list2
print('Concenates list:\n' + str(res))


list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42] 
print("list1 before concatenation:\n" + str(list1))
list1.extend(list2) 
print ("Concatenated list after concatenation:\n"+str(list1))


list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42] 
res = [*list1, *list2] 
print ("Concatenated list:\n " + str(res))


# Write a python program that asks user to enter 3 integers and find the highest value entered.

number1 = int(input("Please enter Your number1: "))
number2 = int(input("Please enter Your number2: "))
number3 = int(input("Please enter Your number3: "))

my_list = [number1, number2, number3]

print(max(my_list))

