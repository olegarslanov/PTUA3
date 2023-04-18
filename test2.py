# flag = True


# for i in range(5):
#     x = int(input())
#     flag = flag and x % 10 == 0

# print(flag)


flag = True


for i in range(0, 10, 10):
    flag = flag and i % 10 == 0

print(flag)
