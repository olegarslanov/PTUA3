# Cafeteria project : Create an live menu and payment system (a.k.a console program) :
# 1
# First the program should ask if table was reserved/ not (Providing your full name) .
# And then if not would assign you a table (there is a specific number single, double or family tables) .
# After table is assigned to you, system should show how many free tables are and how which are
# reserved/occupied. The system must be able to show name/surname of the person of the reserved
#  table (CLI option : enter reserved table number ; OUTCOME: Name/Surname/Time Reserved)
# 2
# After assigning table, system should show different menu options for breakfast, lunch , dinner ,
# drinks (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan must be
# included too in the special menu. All menu items should have weight, preparation time in minutes,
# calories, and price.
# I have to have an option to change the order before the payment section. Thus I can delete,
# add more, update amount of the same order.
# I should be able to choose whatever I want from all menus in one ordering. After I finish,
# I need to see what I chosen, the full payable amount and approx waiting time for the food to
#  be served
# Add an option to add tips (% from the full cost) to the final bill.
# After the payment , system should generate the receipt (logging).


from classes import Table
from typing import List
import datetime

now_hour = (lambda t: t.strftime("%H"))(datetime.datetime.now())

print("Welcome to the Cafeteria Management System!")

# Please select an option:

# 1. Reserve a table
# 2. View all available tables
# 3. View all reserved tables
# 4. View your reservations
# 5. Exit

# Your choice:

table = Table()

while True:
    print("Welcome to the Cafeteria Management System!")
    print("Please select an option:")
    print("1. Reserve a table")
    print("2. View all available tables")
    print("3. View all reserved tables")
    print("4. View your reservations")
    print("5. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        table_type = input(
            "Enter table type (single_table, double_table, family_table): "
        )
        table_id = input("Enter table id: ")
        reservation_hour = input("Enter reservation hour (e.g. 10 for 22): ")

        # if table.check_reservation(name, surname, reservation_hour):
        if table.check_table_free(table_type, table_id, reservation_hour):
            table.create_reservation(
                name, surname, reservation_hour, table_type, table_id
            )
            print("Reservation created successfully.")
        else:
            print("Sorry, the table is already reserved for this time.")
        # else:
        #     print("Sorry, you have already reserved a table for this time.")

    elif choice == "2":
        print("Available tables:")
        table.show_free_tables()

    elif choice == "3":
        print("Reserved tables:")
        table.show_reserved_tables()

    elif choice == "4":
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        print("Your reservations:")
        print(table.show_reservations(name, surname))

    elif choice == "5":
        print("Thank you for using Cafeteria Management System!")
        break

    else:
        print("Something wrong")
