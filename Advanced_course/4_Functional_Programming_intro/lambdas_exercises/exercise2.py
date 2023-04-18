# Write a Python program to create a lambda function that adds 15 to a given number passed
# in as an argument, also create a lambda function that multiplies argument x with
# argument y and print the result.

print((lambda x: (x + 15))(2))
print((lambda x, y: x * y)(2, 3))

# 2
# r = lambda a: a + 15
# print(r(10))
# r = lambda x, y: x * y
# print(r(12, 4))
