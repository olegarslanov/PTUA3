# ; В качестве практической работы попробуйте самостоятельно перегрузить оператор сложения.
# ;  Для его перегрузки используется метод __add__(). Он вызывается, когда объекты класса,
# ;   имеющего данный метод, фигурируют в операции сложения, причем с левой стороны. Это
# ;   значит, что в выражении a + b у объекта a должен быть метод __add__(). Объект b может
# ;    быть чем угодно, но чаще всего он бывает объектом того же класса. Объект b будет
# ;    автоматически передаваться в метод __add__() в качестве второго аргумента (первый – self).

# ; Отметим, в Python также есть правосторонний метод перегрузки сложения - __radd__().

# ; Согласно полиморфизму ООП, возвращать метод __add__() может что угодно. Может вообще ничего
# ;  не возвращать, а "молча" вносить изменения в какие-то уже существующие объекты. Допустим,
# ;   в вашей программе метод перегрузки сложения будет возвращать новый объект того же класса.


class Something:
    def __init__(self, value):
        self.value = value

    def __add__(self, b):
        Something(10)
        return b


a = Something(5)
print(a + 20)


# 2
class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)

    def __str__(self):
        rect = []
        for i in range(self.h):
            rect.append(self.s * self.w)
        rect = "\n".join(rect)
        return rect

    def __add__(self, other):
        return Rectangle(self.w + other.w, self.h + other.h, self.s)


a = Rectangle(4, 2, "w")
print(a)
b = Rectangle(8, 3, "z")
print(b)
print(a + b)
print(b + a)
