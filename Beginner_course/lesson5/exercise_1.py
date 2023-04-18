# Write python program that asks user to enter name, surname, age. 
# Put these values into a dictionary and print dictionary


#1
my_dictionary={}
my_dictionary['name'] = input('Please write Your name:')
my_dictionary['surname']=input('Please enter Your surname:')
my_dictionary['age']=input('Please enter Your age:')

print('New dictionary ready:',my_dictionary)



#2
a=input('Please write Your name:')
b=input('Please write Your surname:')
c=input('Please write Your age:')

values = [a, b, c]
keys = ['name','surname','age']
my_dictionary = dict(zip(keys, values))
print(my_dictionary) 
