# Write a Python program to add three given lists using Python map and lambda

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c = [1, 2, 3, 4]

print(list(map(lambda x, y, z: x + y + z, a, b, c)))
print(list(map(lambda x, y, z: [x] + [y] + [z], a, b, c)))
