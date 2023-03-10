# *args and **kwargs

#1
from typing import Any

def check_arguments(mandatory: Any, *args, **kwargs) -> None:
    print (mandatory)
    if args:
        print (args)
    if kwargs:
        print (kwargs)

check_arguments(101,102,name="")

#2
def my_func(a:int, b:int, *args, c: int = 5, d: int = 9, **kwargs) -> None:
    print (a, b)
    print (args)
    print (c, d)
    print (kwargs)

my_func(1, 2, 3, 4, 5, e=6, f = 7)




#Lambda funkcija (tai paprasta primityvi funkcija)

#1
multiplication = lambda x,y : x*y
print(multiplication(3,4))


#2
from typing import Callable

def my_func(n: int) -> Callable:
    return lambda a,b,c: (a+b+c)*n

my_doubler= my_func(10)

print(my_doubler(10,5,3))






