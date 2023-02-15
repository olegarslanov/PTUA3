# Python Data Structure - List or what in other programming languages is called an array.


# Special python lists methods:

# .append() that allows to insert an item into the list: append()
my_list = []

name='Tom'
my_list.append(name)
print(my_list)   #['Tom']

# .count(obj) allows us to calculate the frequency of the item within the list

my_list = [1, 1, 2 ,3 ,4 ,5]
print(my_list.count(1))   #2

# .insert() as we have seen append always adds the value to the lists end, .insert() allows us to add the value to which ever index we want:

my_list = [1, 1, 2 ,3 ,4 ,5]
my_list.insert(1,50)
print(my_list) # [1, 50, 1, 2, 3, 4, 5]

# .remove() with this method we will simply drop a particular value from the list:

my_list = [1, 1, 2 ,3 ,4 ,5]
my_list.remove(1)
print(my_list)    #[1,2,3,4,5]





# Python built-in List functions:

# "len()"" Note that we do not have the "." symbol now, meaning that there are standalone functions that do not belong to a particular data type.

my_list = ["name", 123, None, True]
print(len(my_list))    # 4

# "max" if you have list of int, float values you may find out maximum value with this function:

my_list = [50, 99, 1, -50]
print(max(my_list))     #99

# "min" if you have list of int, float values you may find out minimum value with this function:

my_list = [50, 99, 1, -50]
print(min(my_list))    #-50



# iterating over elements within the list

my_list = [1,200,-15,4,666]

for item in my_list:
    
    print(item + 15)


# changing an existing value within the list

my_list = [1, 2, 3]
my_list[2] = 5
print(my_list)       #[1,2,5]

# slicing

my_list = ["first", "second", "third"]
print(my_list[-1])
print(my_list[:1])
print(my_list[::2])
print(my_list[::-1])
print(my_list[0:2])   # items from index 0 to index 1 # ['first', 'second']


# operator "in" with Lists

my_list = [1, 2, 3]
print(1 in my_list)    # True


