# pylint: disable - all

# 1
# class Circle:
# def print_my_name():
#     print("Circle")

# def print_my_name(self):
#     print(self.name)


# 2
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, mileage: int) -> None:
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            raise ValueError("You can't roll back an odometer!")

    def drive(self, miles: int) -> None:
        self.update_odometer(self.odometer_reading + miles)


car = Car("Honda", "Civic", 2000)

car.update_odometer(10000)
car.drive(2000)

print(car.odometer_reading)
