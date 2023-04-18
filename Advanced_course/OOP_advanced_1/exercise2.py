# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.


class Vehicle:
    fare_charge = 100

    def __init__(
        self,
        name: str,
        year: int,
        price: float,
        lifetime: int,
        energy_source: str,
        max_speed: int,
        mileage: int,
        seating_capacity: int,
    ) -> None:
        self.name = name
        self.year = year
        self.price = price
        self.lifetime = lifetime
        self.energy_source = energy_source
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def get_name_year(self):
        return f"Vehicle name is {self.name} and made year is {self.year}"

    def get_year_end_of_use(self):
        year_end_of_use = self.year + self.lifetime
        return year_end_of_use

    def get_energy_source(self):
        return f"Vehicle energy source is {self.energy_source}"

    def get_repair_estimate(self):
        if self.year < 2000:
            repair_estimate = self.price * 0.2
        elif self.year > 2000:
            repair_estimate = self.price * 0.1
        return repair_estimate

    def get_mileage(self):
        return f"Vehicle mileage is {self.mileage}"

    def get_fare_charge_total(self):
        fare_charge_total = self.seating_capacity * Vehicle.fare_charge
        return fare_charge_total


class Bus(Vehicle):
    coef = 1.1

    def __init__(
        self,
        name: str = "VW",
        year: int = 2010,
        price: float = 25000,
        lifetime: int = 15,
        energy_source: str = "gasoline",
        max_speed: int = 150,
        mileage: int = 100000,
        seating_capacity: int = 25,
        wc_exists: bool = True,
    ):
        self.wc_exists = wc_exists
        super().__init__(
            name,
            year,
            price,
            lifetime,
            energy_source,
            max_speed,
            mileage,
            seating_capacity,
        )

    def get_fare_charge_total(self):
        fare_charge_total = self.seating_capacity * Vehicle.fare_charge * Bus.coef
        return fare_charge_total


class Taxi(Vehicle):
    def __init__(self, seating_capacity: int) -> None:
        self.seating_capacity = seating_capacity
        Vehicle.__init__(
            self,
            name="Ford",
            year=2012,
            price=650,
            lifetime=11,
            energy_source="gasoline",
            max_speed=85,
            mileage=50000,
            seating_capacity=seating_capacity,
        )

    def get_fare_charge_total(self):
        fare_charge_total = self.seating_capacity * Vehicle.fare_charge
        return fare_charge_total


class Train(Vehicle):
    pass


bus1 = Bus("Ikarus", 2005, 15000, 25, "gasoline", 150, 100000, 10)


vehicle1 = Vehicle("Honda", 2010, 10000, 20, "gasoline", 150, 200000, 10)
bus2 = Bus(seating_capacity=50)
taxi1 = Taxi(4)

print(bus2.get_fare_charge_total())
# print(vehicle1.get_fare_charge_total())
print(taxi1.get_fare_charge_total())

print(vehicle1.get_repair_estimate())

print(bus2.get_mileage())
print(vehicle1.get_mileage())


print(f"vehicle1 is Vehicle: {isinstance(vehicle1, Vehicle)}")
print(f"bus1 is Vehicle: {isinstance(bus1, Vehicle)}")
print(f"bus1 is Bus: {isinstance(bus1, Bus)}")
print(f"vehicle1 is Bus: {isinstance(vehicle1, Bus)}")
