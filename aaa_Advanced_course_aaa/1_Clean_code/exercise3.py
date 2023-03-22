def greet_user(age: int) -> str:
    eligible_to_enter = age >= 21
    if eligible_to_enter:
        return "Welcome"
    return "Access denied"


print(greet_user(21))


# Buvo:
# def Greet_User(age):
#     eligiebleTo_enter = age > 21

#     if eligiebleTo_enter == True:
#         print("Welcome")
#     if eligiebleTo_enter == False:
#         print("Access denied")
