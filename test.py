# 4 Padariau, kad tikrintu 1 stala rezervacija pagal name and surname ir time
from typing import List
import datetime

now_hour = (lambda t: t.strftime("%H"))(datetime.datetime.now())
now_hour = int(now_hour)


class Reservation:
    def __init__(self, name: str, surname: str, reservation_hour: int) -> None:
        self.name = name
        self.surname = surname
        self.reservation_hour = reservation_hour


class Table:
    def __init__(self, table_number) -> None:
        self.table_number = table_number
        self.reservations: List[Reservation] = []

    def create_reservation(self, name, surname, reservation_hour):
        reservation = Reservation(name, surname, reservation_hour)
        self.reservations.append(reservation)

    def check_aviability(self, name, surname, now_time):
        for reservation in self.reservations:
            if (
                reservation.name == name
                and reservation.surname == surname
                and reservation.reservation_hour == now_time
            ):
                return False
        return True


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


table = Table("1")
table.create_reservation("Oleg", "Arslanov", 18)
table.create_reservation("Luiz", "Fernandez", 21)
print(table.check_aviability("Luiz", "Fernandez", now_hour))


#  5 Papildziau, kad patikrintu neturinciam rezervacijos ar tam laikui laisvas stalas
# please enter number of guests
# check, if guest <= number of seat and time != reservation time got message to assign table
# if not got message sorry we dont have  free tables

from typing import List
import datetime

now_hour = (lambda t: t.strftime("%H"))(datetime.datetime.now())


class Cafeteria:
    # def __init__(self):
    #     pass

    single_table = [1]
    double_table = [2, 3]
    family_table = [4, 5, 6]
    # meniu


class Reservation:
    def __init__(self, name: str, surname: str, reservation_hour: int) -> None:
        self.name = name
        self.surname = surname
        self.reservation_hour = reservation_hour


class Table:
    def __init__(self, number_of_seats: int) -> None:
        self.number_of_seats = number_of_seats
        self.reservations: List[Reservation] = []

    def create_reservation(self, name, surname, reservation_hour):
        reservation = Reservation(name, surname, reservation_hour)
        self.reservations.append(reservation)

    def check_aviability(self, name: str, surname: str, now_hour: int):
        for reservation in self.reservations:
            if (
                reservation.name == name
                and reservation.surname == surname
                and reservation.reservation_hour == now_hour
            ):
                print(
                    f"Welcome to our Cafeteria {name} {surname}. You have reservation"
                )
                return False

        print(f"Welcome to our Cafeteria {name} {surname}. You dont have reservation")
        return True

    # def check_aviability(self, guests_quant):
    #     for reservation in self.reservations:
    #         elif (reservation.reservation_hour != now_hour):
    #             print("But good news for You, we have table free. Please sit down")


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


single_table = Table(1)
double_table = Table(2)
family_table = Table(5)

family_table.create_reservation("Oleg", "Arslanov", 18)
family_table.create_reservation("Luis", "Fernandez", 21)

family_table.check_aviability(
    input("Please enter name:"),
    input("Please enter surname:"),
    int(now_hour),
)
