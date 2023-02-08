
# 1. Create a list of different types of python objects, and
#  print all the types. 


my_list = [1 , 2.5 , 'Andy', {'name':'Albert','age':'78'}]

for element in my_list:
   print (type(element))


# 2. print all the items separated with "|"


print(*my_list, sep='|')


# 3. create a list of floats with 3 decimal points, create 
# another list with all the values rounded to 2 decimals.

list_floats=[4.568,5.678,2.547]

for element in list_floats:
    print(round((element),2))


# 4. Create a list with student names and sort them, print 
# the result to the terminal.

students_list=['Petras','Alena','John','Kazys']
print(sorted(students_list))
print(sorted(students_list, reverse=True))

# 5. write a program that allows user to write in any float 
# number and then round it.

float = input("Please enter any number:")
if float > 0:
    print(round(float),2)


list_floats=[4.568,5.678,2.547]

for element in list_floats:
    print(round((element),2))




