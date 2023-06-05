# Create at least 5 different functions and try to handle at least 5 built-in Python
#  Exceptions.

from typing import Union
from typing import Optional

# 1
def add_any (num_1:float,num_2:float)->float:
    sum=num_1+num_2
    return sum
   
try:
    my_new_sum = add_any('a', 1)
    print("try.",my_new_sum)

except TypeError as e:
    print(f"except. def add_any. error: {e}")


else:
    print("else. Yes I did it")

finally:
    print('\nfinally. Printed anyways')


#2
def div_any(num_1: Union[int, float], num_2: Union[int, float]) -> Union[int, float]:
    div = num_1/num_2
    return div

try:
    my_new_div = div_any('a' , 2)
    print(my_new_div)

except TypeError as e:
    print(f"Error 123 :{e}")


#3
def print_smth ()->str:
   print("Hello world!")


try:
    print_smt()

except NameError as e:
    print(f"Error :{e}")


#4
def get_random_number()->int:
  import random
  a=(random.randint(0, a))
  return a

try:
  new_random_number=get_random_number(imp,b)
  print(new_random_number)

except Exception as e:
  print(f"Error : {e}")


#5
def round_num (num)->float:
   num=round(num, 2)
   return num

try:
    my_num = round_num(143.269992, 1)
    print(my_num)

except Exception as e:
    print(f"except. def roun_num. error: {e}")


else:
    print("else. Yes I did it")

finally:
    print('\nfinally. Printed anyways')

#6
empoyer_dict = {"Name": "Antanas", "ID":256}

try:
    employer_id = employer_dict["ID"]
    print(employer_id)

    emp_role = employer_dict["Role"]
    print(emp_role)

except KeyError as e:
    print(f"Key Not Found in Employee Dictionary: {e}")