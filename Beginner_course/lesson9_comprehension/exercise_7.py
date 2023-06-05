#Create a dictionary with 5 key:value pairs, Keys must be strings, values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)


my_dict = {
    "Names":12,
    "Surnames":23,
    "Towns":35,
    "Languages":45,
    "Religions":59
    }


my_new_dict={}
for key, value in my_dict.items():
    my_new_dict[key.upper()] =int(str(value)[::-1])
print(my_new_dict)


# Dictionary comprehensions:

my_new_dict={key.upper():int(str(value)[::-1]) for key,value in my_dict.items()}
print(my_new_dict)



