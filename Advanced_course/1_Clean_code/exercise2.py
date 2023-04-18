def greet_person(full_name: str) -> None:
    """Function greets a person given full name as a string"""

    print(f"Hello {full_name.split()[0]} {full_name.split()[1]}, how are you today?")


greet_person("Oleg Arlanov")


# Buvo:
# def x(a):
#     """Function greets a person given full name as a string"""

# print(f"Hello {a.split()[0]} {a.split()[1]}, How are you today?")
