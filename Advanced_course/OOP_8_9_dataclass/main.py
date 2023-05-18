# 1
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str


person = Person("John Doe", 30, "johndoe@example.com")
print(person.name)  # Output: John Doe


# 2
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


point = Point(3, 4)
print(point.distance_from_origin())  # Output: 5.0
