# Create a program with 3 different modules:

# first, to do basic tasks with strings
# second, basic tasks with lists.
# third, basic tasks with numbers
# Import them as modules to the main.py module and show calculations.




import exercise_2b as strings

import exercise_2c as lists

import exercise_2d as numbers


print(strings.leet_text("What You wanna do"))

print(numbers.add(1,2))

print(lists.count_list(["1","2","m", 4, False]))


