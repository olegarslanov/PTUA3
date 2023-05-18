from _reservation import Tables
import _helpers as h
from datetime import datetime

tables = Tables()

current_time = datetime.now().strftime("%H:%M")

print("Welcome to our cafeteria!")

user_answer = input("Do you want to make a new reservation?(Yes/No): ").strip().lower()
if h.identify_input(user_answer):
    print("Here are our free tables:")
    tables.show_free_tables()
    print("We will need some information to make a new reservation")
    name = input("Please enter name: ")
    surname = input("Please enter surname:")
    table_type = input("Please enter table type:")
    table_id = input("Please enter table id:")
    time = input("Please enter hour:")
    tables.reserve_table(
        name=name, surname=surname, table_type=table_type, table_id=table_id, time=time
    )
    print(tables.show_reservation(name=name, surname=surname))
else:
    print("Choose the table you want from the free tables list")
    print("Here are our free tables at the moment:")
    tables.show_free_tables()
    name = input("Tell us your name: ").strip()
    surname = input("And surname: ").strip()
    table_type = h.get_valid_table_type()
    table_id = h.get_valid_table_id()
    time = current_time
    tables.reserve_table(
        name=name,
        surname=surname,
        table_type=table_type,
        table_id=table_id,
        time=time,
    )
    print(tables.show_reservation(name=name, surname=surname))
