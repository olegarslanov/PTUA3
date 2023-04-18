# Find all of the numbers from 1-1000 that are divisible by 6


numbers=[]
for number in range (6,1000,6):
    numbers.append(number)
print(numbers)

#comprehension
numbers=[number for number in range(6,1000,6)]
print(numbers)

