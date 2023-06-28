# Define a property that must have the same value for every class instance (object)


class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus1 = Bus("School Volvo", 180, 12)
car1 = Car("Audi Q5", 240, 18)

print(bus1.color, bus1.name, "Speed:", bus1.max_speed, "Mileage:", bus1.mileage)
