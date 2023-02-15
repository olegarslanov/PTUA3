# print all the items separated with "|"

my_list = [1 , 2.5 , 'Andy', {'name':'Albert','age':'78'}]


print ("printing lists separated by '|'")
print(*my_list, sep='|')

print('|'.join(map(str, my_list))) 

