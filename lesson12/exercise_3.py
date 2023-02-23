# Create a mini python program which would take two numbers as an input and 
# would return their sum, subtraction, division, multiplication. Handle 
# all possible errors that may occur.

#1
x = float(input("Please enter first number:"))
y = float(input("Please enter second number:"))

def calculator (x:float, y:float) -> float:
    try:
        sum = x + y
        sub = x - y
        div = x / y
        multi = x * y
        return (sum, sub, div, multi)

    except ZeroDivisionError:
        print('Divisor is zero; Division is impossible')
    
    except Exception as e:
        print(f"Something wrong! {e}")
    
    else:
        print("Can run here something else!")

    finally:
        print(sum, sub, div, multi)

print(calculator(x,y)) 


#2
from typing import Union

def calc(x: float, y: float) -> dict[str, Union[int, float]]:
    sum = x + y
    sub = x-y
    div = x / y
    multi = x * y
    calc_result = {'sum of numbers:': sum, 'subtraction of numbers:': sub, 'division of numbers': div, 'multiplication of numbers:':multi}
    return calc_result

def format_print_dict (calc_result: dict[str, Union[int, float]]) -> None:
    for key, value in calc_result.items():
        print(f"{key}:{value}")

try:
    x = float(input('Please enter first number:'))
    y = float(input('Please enter second number:'))
    result = calc(x, y)
    format_print_dict(result)

except ZeroDivisionError:
    print('Divisor is zero; Division is impossible')
    
except Exception as e:
    print(f"Something wrong! {e}")
    
else:
    print("You can program more things in 'else' field")



