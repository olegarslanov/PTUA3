# Define a Shape class with the following attributes and methods:
# A name attribute, which is a string that represents the name of the shape.
# A sides attribute, which is an integer that represents the number of sides of the shape.
# An area method, which returns the area of the shape.

# Then, define a Rectangle class that inherits from the Shape class and has the following
# attributes and methods:
# A width attribute, which is a float that represents the width of the rectangle.
# A height attribute, which is a float that represents the height of the rectangle.
# An init method that initializes the name, sides, width, and height attributes.
# An area method that overrides the area method of the Shape class and returns the area of
#  the rectangle.

# Finally, define a Square class that inherits from the Rectangle class and has the following
#  attributes and methods:
# A side_length attribute, which is a float that represents the length of the sides of the square.
# An init method that initializes the side_length attribute and calls the init method of the
# Rectangle class to initialize the name, sides, width, and height attributes.


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def get_area(self):
        return self.sides**2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        # super().__init__(name=self.name, sides=self.sides)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_lenght: float) -> None:
        self.side_lenght = side_lenght

    def get_area(self):
        return self.side_lenght**2


shape_1 = Shape("foo", 100)
print(shape_1.get_area())
print(shape_1.name)

rectangle_1 = Rectangle(10, 5)
print(rectangle_1.get_area())
# print(rectangle_1.name)

square_1 = Square(10)
print(square_1.get_area())


# class Shape:
#     def __init__(self, name: str, sides: int) -> None:
#         self.name = name
#         self.sides = sides

#     def get_area(self):
#         return self.sides**2


# class Rectangle(Shape):
#     def __init__(self, width: float, height: float) -> None:
#         # super().__init__(name=self.name, sides=self.sides)
#         self.width = width
#         self.height = height

#     def get_area(self):
#         return self.width * self.height


# class Square(Rectangle):
#     def __init__(self, side_lenght: float) -> None:
#         self.side_lenght = side_lenght

#     def get_area(self):
#         return self.side_lenght**2


# shape_1 = Shape("foo", 100)
# print(shape_1.get_area())
# print(shape_1.name)

# rectangle_1 = Rectangle(10, 5)
# print(rectangle_1.get_area())
# # print(rectangle_1.name)

# square_1 = Square(10)
# print(square_1.get_area())
