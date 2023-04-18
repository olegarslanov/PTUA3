#  create a number guessing game from 1-10, with random library. 
# (IDEA FOR LATER MAYBE)

print("It is guessing game from 1 to 10. You must guess random number")

import random
random_number=random.randint(0,10)

while True:
    user_number=int(input('Please guess number:'))
    if user_number==random_number:
         print("Congratulations. You won :)")
         break








