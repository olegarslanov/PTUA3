def do_twice(func):
    def wrapper_do_twice(
        *args, **kwargs
    ):  # (использовать *args* *kwargs во внутренней функции-оболочке. Затем он примет произвольное количество позиционных и ключевых аргументов.)
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice  # funkcijos do_twice issipletimas(debugging eina iskart i sitos funkcijos vidu), t. y. paleidziant funkcija "return_greeting"
def return_greeting(name):
    print("Creating greeting")
    print("test")
    # return f"Hi {name}"


return_greeting("World")
