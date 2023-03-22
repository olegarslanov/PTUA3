# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


Ferrari = Vehicle(200, 100000)
Mazda = Vehicle(150, 150000)


print(Ferrari.max_speed)








