# Papildoma info:
# 1
# my_function = parent(1)
# my_function("Vytautas")
# arba tas pats kitaip
# parent(1)("Vytautas")
# 2
# Jeigu nurodoma funkcija be skliaustu, tai reiskia kad Jus grazinat nuoroda i funkcija. Jeigu funkcija su skliautais tai bus vykdoma funkcija.


# 1 Pavyzdis
# a) be dekoratoriaus
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(
    say_whee
)  # pakeiciam originaliąją funkciją say_whee i jos dekoruota versija. Tokiu budu iskvieciu jau ne originalia funkcija, o jos dekoruota versija

say_whee()

# atsakymas:
# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.


# b) su dekoratoriumi
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator  # sutrumpinta versija "say_whee = my_decorator(say_whee)""
def say_whee():
    print("Whee!")


say_whee()

# @my_decorator это просто более простой способ сказать say_whee = my_decorator(say_whee)


# 3 Pavyzdis
def do_twice(func):
    def wrapper_do_twice(
        *args, **kwargs
    ):  # (использовать *args* *kwargs во внутренней функции-оболочке. Затем он примет произвольное количество позиционных и ключевых аргументов.)
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


return_greeting("World")


# ////////

# def decorator(func):
#     def wrapper():
#         print("Prieš vykdant funkciją")
#         func()
#         print("Po vykdymo funkcijos")

#     return wrapper


# @decorator # leidžia pridėti papildomą funkcionalumą esamoms funkcijoms arba klasėms, išplėsti jų elgesį ar pakeisti jų veikimą, nes modifikuojamos funkcijos ar klasės yra perduodamos dekoratoriaus kaip argumentas.
# def my_function():
#     print("Įprasta funkcija")


# my_function()


# //////////

import random

PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
