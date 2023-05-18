from typing import List


class Cafeteria:
    pass


class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Reservation:
    def __init__(
        self,
        name: str,
        surname: str,
        reservation_hour: str,
        table_type: str,
        table_id: str,
    ) -> None:
        self.name = name
        self.surname = surname
        self.reservation_hour = reservation_hour
        self.table_type = table_type
        self.table_id = table_id


class Table:
    def __init__(self) -> None:
        self.tables = {
            "single_table": {
                "nr1": {
                    "reserved": False,
                    "name": "",
                    "surname": "",
                    "reservation_hour": "",
                },
                "nr2": {
                    "reserved": False,
                    "name": "",
                    "surname": "",
                    "reservation_hour": "",
                },
            },
            "double_table": {
                "nr3": {
                    "reserved": False,
                    "name": "",
                    "surname": "",
                    "reservation_hour": "",
                },
                "nr4": {
                    "reserved": False,
                    "name": "",
                    "surname": "",
                    "reservation_hour": "",
                },
            },
            "family_table": {
                "nr5": {
                    "reserved": False,
                    "name": "",
                    "surname": "",
                    "reservation_hour": "",
                },
                "nr6": {
                    "reserved": False,
                    "name": "",
                    "surname": "",
                    "reservation_hour": "",
                },
                "nr7": {
                    "reserved": True,
                    "name": "Oleg",
                    "surname": "Arslanov",
                    "reservation_hour": "07",
                },
            },
        }
        self.reservations: List[Reservation] = []

    def check_reservation(self, name: str, surname: str, reservation_hour) -> bool:
        for reservation in self.reservations:
            if (
                reservation.name == name
                and reservation.surname == surname
                and reservation.reservation_hour == reservation_hour
            ):
                # print(
                #     f"Welcome to our Cafeteria {name} {surname}. You have reservation"
                # )
                return False

        # print(f"Welcome to our Cafeteria {name} {surname}. You dont have reservation")
        return True

    def check_table_free(
        self, table_type: str, table_id: str, reservation_hour
    ) -> bool:
        if (
            self.tables[table_type][table_id] != True
            and self.tables[table_type][table_id][reservation_hour] != reservation_hour
        ):
            return False
        return True

    def create_reservation(
        self,
        name: str,
        surname: str,
        reservation_hour: str,
        table_type: str,
        table_id: str,
    ):
        reservation = Reservation(name, surname, reservation_hour, table_type, table_id)
        self.reservations.append(reservation)

    def show_free_tables(self) -> None:
        for key, value in self.tables.items():
            for table_id, table_status in value.items():
                if table_status == False:
                    print(f"{key}: {table_id} is {table_status}")

    def show_reserved_tables(self):
        for key, value in self.tables.items():
            for table_id, table_status in value.items():
                if table_status == True:
                    print(f"{key}: {table_id} is {table_status}")

    def show_reservations(self, name: str, surname: str):
        for reservation in self.reservations:
            if reservation.name == name and reservation.surname == surname:
                return f"{name} {surname} reserved a {reservation.table_type} type table for {reservation.reservation_hour}"
            else:
                return "Reservation was not found"
