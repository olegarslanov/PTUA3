# Create a variables containing strings for username and 
# password. Start Endless loop allowing to enter username and 
# password. If credentials are correct stop endless loop and print 
# greeting message.


user_name=("Oleg")
user_pass=("password")

while True:
    user_input=input("Enter your user name: ")
    pass_input=input("Enter your password: ")
    if user_input == user_name and user_pass==pass_input:
        print("Welcome to the program")
        break
    print('Program dont alow You enter!')


