
# Create two lists and add them together, make sure it works the
#  way you want it to.


my_list1 = [1,2,3]
my_list2 = [4,5,6]
res=my_list1+my_list2
print('Concenates list:\n' + str(res))


list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42] 
print("list1 before concatenation:\n" + str(list1))
list1.extend(list2) 
print ("Concatenated list after concatenation:\n"+str(list1))


list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42] 
res = [*list1, *list2] 
print ("Concatenated list:\n" + str(res))


# \n    it is mean start from new line