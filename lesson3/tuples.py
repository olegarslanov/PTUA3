# Tuple is immutable. Meaning that we have an object that contains multiple values, they can be duplicated, almost all characteristics are similar except that the items in Tuple by design cannot be changed.
 
empty_tuple = ()
tuple_single_item = (1,)
another_tuple = (1, 2, 3)

print(tuple_single_item)

# Operations
# those are simply exactly the same, except that you are unable to mutate the tuple. If you try doing so, you will get an error:
my_tuple = (1, 2, 3)
my_tuple[0] = 500 # TypeError: 'tuple' object does not support item assignment




# my_tuple = ("aaa", 2, 3)

# my_tuple[0] = 150

# print (my_tuple)
# print (type (my_tuple))

