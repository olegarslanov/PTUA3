
# Lists comprehension ---------

# Example 1

squares = []
for number in range(10):
    squares.append(number*number)
print(squares)

#list comprehension
squares = [number*number for number in range(10)]
print(squares)


# Example 2

squares = []
for number in range(10):
    if number!=5:
        squares.append(number * number)
print(f'first:{squares}')

#list comprehensio
squares = [number * number for number in range(10) if number != 5]
print(squares)


# Dictionary comprehension -------

# Example 3

dict = {}
for i in range(10):
    dict[i] = i * i

print(dict)


#dictionary comprehension
squares = {i: i * i for i in range(10)}
print(squares)

# Example 4
# program without perfect square of 5

dict = {}
for i in range(10):
    if i!=5:
        dict[i] = i * i

print(dict)


#dictionary comprehension
squares = {i: i * i for i in range(10) if i!=5}
print(squares)


# Example 5
# only odd numbers

dict = {}
for i in range(1,10,2):
    dict[i] = i * i

print(dict)


#dictionary comprehension
squares = {i: i * i for i in range(1,10,2)}
print(squares)


# Example 6

values = ["a", "b", "c"]

index = 0
for value in values:
    print(index, value)
    index += 1


# comprehension
for count, value in enumerate(values):
    print(count, value)

for count, value in enumerate(values, start=1):
    print(count, value)




# Import math

import math

print(math.ceil(6.1))

print(math.floor(11.1))

import math
print (math.sqrt(9))


