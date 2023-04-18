# import os


# USER = os.getenv("USER")
# TOKEN = os.getenv("TOKEN")


# print(USER)
# print(TOKEN)


# import os

# os.environ["password"] = "you_will_never_find_out"

# print(os.getenv("password"))


import os

USER = os.environ.get("USER", "Not Set")
print(USER)
