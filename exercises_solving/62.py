
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 0 , 00]


value = random.choice(numbers)


print("Random number:", value)
print("Number wins:", value)


# value = [1, 3, 5, 7, 9,\
#         12, 14, 16, 18,\
#         19, 21, 23, 25, 27,\
#          30, 32, 34, 36]

if value % 2 == 1 and value >=1 and value <= 9 or \
    value % 2 == 0 and value >= 12 and value <= 18 or \
    value % 2 == 1 and value >= 19 and value <= 27 or \
    value % 2 ==0 and value >= 30 and value <= 36:
    print("Wins red color")
else:
    print("Wins black color")


if value % 2 == 0:
    print("Wins number is even")
elif value == 0:
    pass
elif value == 00:
    pass
else:
    print("Wins number is odd")


if value <= 18:
    print("Wins number from 1 to 18")
elif value == 0:
    pass
elif value == 00:
    pass
else:
    print("Wins number from 19 to 36")















