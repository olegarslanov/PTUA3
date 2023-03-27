# Create a Calculator program : it should contain abstract class with methods
#  (abstract and not), base class, geometry, arithmetic calculator classes.
#  Every subclass should have at least 5 methods to make some meaningful calculus operations.


import math
from abc import ABC, abstractmethod
from typing import List


class Calculator(ABC):
    def __init__(self, operation_category: str) -> None:
        self.operation_category = operation_category

    @abstractmethod
    def get_area_rectangle(self) -> float:
        pass

    @abstractmethod
    def get_addition(self) -> float:
        pass

    def get_operation_category(self) -> str:
        return self.operation_category


class Geometry(Calculator):
    def __init__(
        self,
        operation_category="geometry",
        radius: float = 0,
        width: float = 0,
        height: float = 0,
        plan_coordinate1: List[float] = [0, 0],
        plan_coordinate2: List[float] = [0, 0],
        a: float = 0,
        b: float = 0,
        c: float = 0,
        f: float = 0,
        e: float = 0,
        h: float = 0,
    ) -> None:
        self.width = width
        self.height = height
        self.radius = radius
        self.plan_coordinate1 = plan_coordinate1
        self.plan_coordinate2 = plan_coordinate2
        self.a = a
        self.b = b
        self.c = c
        self.f = f
        self.e = e
        self.h = h
        super().__init__(operation_category)

    def get_area_rectangle(self):
        return self.width * self.height

    def get_addition(self):
        pass

    def get_area_round(self):
        return math.pi * self.radius**2

    def get_area_trapecia(self):
        area_trapecia = ((self.f + self.e) / 2) * self.h
        return area_trapecia

    def get_triangle_area(self):
        s = (self.a + self.b + self.c) / 2
        triangle_area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return triangle_area

    def get_line_lenght_plan(self):
        line_lenght_plan = math.dist(self.plan_coordinate1, self.plan_coordinate2)
        return line_lenght_plan


class Arithmetic(Calculator):
    def __init__(
        self, operation_category: str = "arithmetic", x: float = 0, y: float = 0
    ):
        self.x = x
        self.y = y
        super().__init__(operation_category)

    def get_addition(self):
        return self.x + self.y

    def get_area_rectangle(self):
        pass


rectangle1 = Geometry(width=3, height=4)
round1 = Geometry(radius=2)
plan_line = Geometry(plan_coordinate1=[2, 3], plan_coordinate2=[4, 5])
triangle1 = Geometry(a=4, b=3, c=2)
trapecia1 = Geometry(f=5, e=4, h=3)

addition1 = Arithmetic(x=4, y=6)

print(rectangle1.get_area_rectangle())
print(round1.get_area_round())
print(plan_line.get_line_lenght_plan())
print(triangle1.get_triangle_area())
print(trapecia1.get_area_trapecia())

print(addition1.get_addition())
