class MyClass:
    @classmethod
    def my_class_method(cls, arg1: Any, arg2: Any, ...) -> <"class name">
        # code here



class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    @classmethod
    def from_square(cls, side_length: float) -> "Rectangle":
        return cls(side_length, side_length * 2)


rectangle1: Rectangle = Rectangle(3.0, 4.0)
rectangle2: Rectangle = Rectangle.from_square(2.0)

print(rectangle1.area())  # 12.0
print(rectangle2.area())  # 4.0


# class Square(Rectangle):
#     def __init__(self, side_lenght):
#         self.side_lenght = side_lenght
#         self.width = self.side_lenght * 2

#     def

# rectangle2 = Square(3)
# print(rectangle2.area())
