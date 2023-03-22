# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass
    

vehicle_name = Bus("School Volvo", 180, 12)

print(vehicle_name.name)
print(vehicle_name.max_speed)
print(vehicle_name.mileage)
