# A common template for using the property decorator is:


class C(object):
    # @property palengvina atributu sudaryma klasese (cia iskvieciamas getter, ji nebutina irasyti)
    @property
    def x(self):
        return self._x

    # tikrina ieinancius duomenys, kad jie atitiktu tam tikras salygas
    @x.setter
    def x(self, value):
        self._x = value

    # nebutina irasyti
    @x.deleter
    def x(self):
        del self._x


# 1
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    # @property realiai naudojama kaip getteris, o su setteriu nustatau
    @property
    def area(self) -> float:
        return self.width * self.height


r = Rectangle(3.0, 4.0)
print(r.area)  # output: 12.0


# 2
class Student:
    def __init__(self):
        self._score: int = 0

    # palengvina atributu
    @property
    def score(self) -> int:
        return self._score

    # nustatau kazkokius limitus ar panasiai
    @score.setter
    def score(self, s: int) -> None:
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError("The score must be between 0 ~ 100!")

    @score.deleter
    def score(self) -> None:
        del self._score


Tom = Student()
Tom.score = 99
print(Tom.score)
# ValueError: The score must be between 0 ~ 100!


# 3
class Circle:
    def __init__(self, r):
        self.r = r

    # @property
    # def area(self):
    #     return 3.1415 * self.r**2

    def area(self):
        return 3.1415 * self.r**2


c = Circle(10)
# print(c.area)
print(c.area())
