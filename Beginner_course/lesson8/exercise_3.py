# Generate a dictionary of 10 keys being 1,2,3...10 each of them should store a value 
# of random integer number from 1 to 100.



import random

my_dict={}

for new_key in range(1,11):
    my_dict[new_key] = random.randint(1,100)

print(my_dict)


