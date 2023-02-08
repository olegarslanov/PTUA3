# We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# Create one final dictionary from all those 3.

dic_one={1:10, 2:20}
dic_two={3:30, 4:40}
dic_three={5:50,6:60}

dic_one.update(dic_two)
dic_one.update(dic_three)
print(dic_one)



# Write a Python script to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x*x):
# You can use input to receive the number. Example:
# n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


input_a = int(input('Input number from 1 to universe:'))

dic = {}
for n_value in range(0, input_a + 1):
    dic[n_value] = n_value * n_value

print(dic)


# Write python program that asks user to enter name, surname, age. 
# Put these values into a dictionary and print dictionary


my_dictionary={}
my_dictionary['name'] = input('Please write Your name:')
my_dictionary['surname']=input('Please enter Your surname:')
my_dictionary['age']=input('Please enter Your age:')

print('New dictionary ready:',my_dictionary)


a=input('Please write Your name:')
b=input('Please write Your surname:')
c=input('Please write Your age:')

values = [a, b, c]
keys = ['name','surname','age']
my_dictionary = dict(zip(keys, values))
print(my_dictionary) 

