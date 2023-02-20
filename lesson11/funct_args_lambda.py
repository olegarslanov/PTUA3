
# *args and **kwargs

from typing import Any

def check_arguments(mandatory: Any, *args, **kwargs) -> None:
    print (mandatory)
    if args:
        print (args)
    if kwargs:
        print (kwargs)

check_arguments(101,102,name="")




#Lambda funkcija (paprasta primityvi funkcija)

multiplication = lambda x,y : x*y
print(multiplication())




from typing import Callable

def my_func(n: int) -> Callable:
    return lambda a,b,c: (a+b+c)*n

my_doubler= my_func(10)

print(my_doubler(10,5,3))






