# 1. Find all of the numbers from 1-1000 that are divisible by 6

numbers=[]
for number in range (5,1000,6):
    numbers.append(number+1)
print(numbers)


numbers=[number+1 for number in range(5,1000,6)]
print(numbers)

