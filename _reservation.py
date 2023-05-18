from typing import Union, Dict, Optional, List
from datetime import datetime


class Reservation:
    def __init__(
        self, name: str, surname: str, time: str, table_type: str, table_id: int
    ) -> None:
        self.name = name
        self.surname = surname
        self.time = time
        self.table_type = table_type
        self.table_id = table_id


class Tables:
    def __init__(self) -> None:
        self.tables = {
            "single": {
                1: "free",
                2: "free",
                3: "free",
                4: "free",
            },
            "double": {
                1: "free",
                2: "free",
                3: "free",
            },
            "family": {
                1: "free",
                2: "free",
            },
        }
        self.table_reservations: List[Reservation] = []

    def check_reservation(self, name: str, surname: str) -> bool:
        if self.table_reservations == None:
            return False
        for reservation in self.table_reservations:
            if reservation.name == name and reservation.surname == surname:
                return True

    def check_if_table_free(self, table_type: str, table_id: int) -> bool:
        if self.tables[table_type][table_id] == "free":
            return True
        return False

    def reserve_table(
        self, name: str, surname: str, time: str, table_type: str, table_id: int
    ) -> Optional[str]:
        if self.check_if_table_free(table_type=table_type, table_id=table_id):
            reservation = Reservation(
                name=name,
                surname=surname,
                time=time,
                table_type=table_type,
                table_id=table_id,
            )
            self.table_reservations.append(reservation)
            self.tables[table_type][table_id] = "reserved"
        else:
            return "Table is already reserved"

    def show_free_tables(self) -> None:
        for key, value in self.tables.items():
            for table_id, table_state in value.items():
                if table_state == "free":
                    print(f"{key}: {table_id} is {table_state}")

    def show_reserved_tables(self) -> str:
        for key, value in self.tables.items():
            for table_id, table_state in value.items():
                if table_state == "reserved":
                    print(f"{key}: {table_id} is {table_state}")

    def show_reservation(self, name: str, surname: str) -> str:
        if self.table_reservations == None:
            return "We are sorry, reservation was not found"
        for reservation in self.table_reservations:
            if reservation.name == name and reservation.surname == surname:
                return f"{name} {surname} reserved a {reservation.table_type} type table for {reservation.time} o'clock"
            else:
                return "We are sorry, reservation was not found"
