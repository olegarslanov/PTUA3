# Create a function that returns only strings with unique characters.

#1
import random
import string

for i in range(1):
    # get random string of length 8 without repeating letters
    result_str = ''.join(random.sample(string.printable, 8))
    print(result_str)

#2
strings_list=["Oleg","Tatjana","Agata","Radomir","Milada"]


def unique_values(str_list: list[str])->list[str]:
    new_str_list=[]

    for value in str_list:
        if len(set(value))==len(value):
            new_str_list.append(value)

    return new_str_list

print("New string list:", unique_values(strings_list))

