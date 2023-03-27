from dotenv import dotenv_values

config = dotenv_values(".env")

username1 = input("Please enter username:")
password1 = input("Please enter password:")

if username1 == config["username"] and password1 == config["password"]:
    print("ACCESS GRANTED")
else:
    print("WRONG CREDENTIALS")
