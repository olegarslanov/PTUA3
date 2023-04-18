# Update previous task with possible raise exception.


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
    if y==0:
        raise ZeroDivisionError('Divisor is zero; Division is impossible')
    result = calc(x, y)
    format_print_dict(result)
    

except ZeroDivisionError as error:
    print(error)
    
# except Exception as e:
#     print(f"Something wrong! {e}")
    
# else:
#     print("You can program more things in 'else' field")

finally:
    print("Finally")