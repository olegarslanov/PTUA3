# Write a Python program to add two given lists and find the difference between lists.
# Use map() function.


a = [1, 2, 3, 4]
b = [1, 3, 3, 4]


print(list(map(lambda x, y: x + y, a, b)))
print(list(map(lambda x, y: x - y, a, b)))
