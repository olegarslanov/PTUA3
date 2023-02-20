# Create at least 5 different functions by your own and test it.

#1
def print_smth ()->str:
   print("Hello world!")

print_smth()


2
def sum (num1,num2)->int:
  sum=num1+num2
  print(sum)
  return sum

sum(1,2)

#3
def get_random_number()->int:
  import random
  a=(random.randint(0, 10))
  return a
  
print(get_random_number())

#4
def string_upper (input_string)->str:
    upper_input=input_string.upper()
    print(upper_input)
    return upper_input

string_upper("i want understand functions and use them")

#5
def type_indent (user_input)->list:
   a=type(user_input)
   print(a)

type_indent([1.25,5])

#6
def round_num (num)->float:
   num=round(num,2)
   print(num)
   return

round_num(10.254859)

#7
def add_numbers(a,b,c)-> int:
   return int(a)+int(b)+int(c)

print(add_numbers(1,2,3))


