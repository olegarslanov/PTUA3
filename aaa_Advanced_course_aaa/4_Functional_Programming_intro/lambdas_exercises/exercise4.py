# Write a Python program to square and cube every number in a given list of integers using Lambda

list1 = [1, 2, 3, 4]
print(list(map(lambda x: (x**2, x**3), list1)))

# 2
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square_nums = list(map(lambda x: x**2, nums))
# print(square_nums)
# cube_nums = list(map(lambda x: x**3, nums))
# print(cube_nums)
