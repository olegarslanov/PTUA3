from typing import Union


def divider(number: Union[float,int]) -> None:
    return number/2 if isinstance(number, float) else number//2

# isinstance(number,float) - tikrina ar kintamasis"number" tai float. Jei tai float grazins 'True'

try:
    my_divided_number=divider(5)
    print(my_divided_number)
    print(my_divided_number/0)

except Exception as e:
    print(f'Error: {e}')

else:
    print("Success")

finally:
    print('\n I dont care: I am printed anyways')


