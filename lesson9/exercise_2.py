# 2. Find all number from 1-1000 that have 9 in them.

num_list=[]
for number in range (8,1000,10):
    num_list.append(number+1)
print(num_list)


# comprehension

num_list=[number+1 for number in range (8,1000,10)]
print(num_list)