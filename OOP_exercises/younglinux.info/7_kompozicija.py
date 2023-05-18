# требуется написать программу, которая вычисляет площадь обоев для оклеивания помещения.
# При этом окна, двери, пол и потолок оклеивать не надо.


# class WinDoor:
#     def __init__(self, w, h):
#         self.square = w * h


# class Room:  # klass "Room" eto klass-konteiner dlja okon i dverej
#     def __init__(self, x, y, z):
#         self.square = 2 * z * (x + y)
#         self.wd = []

#     def add_wd(self, w, h):
#         self.wd.append(WinDoor(w, h))

#     def work_surface(self):
#         netto_square = self.square
#         for i in self.wd:
#             netto_square -= i.square
#         return netto_square


# r1 = Room(6, 3, 2.7)
# print(r1.square)  # выведет 48.6
# r1.add_wd(1, 1)
# r1.add_wd(1, 1)
# r1.add_wd(1, 2)
# print(r1.work_surface())  # выведет 44.6


# 2 Исправьте код так, чтобы у объектов Room были только четыре поля – width, lenght,
#  height и wd. Площади (полная и оклеиваемая) должны вычислять лишь при необходимости
# путем вызова методов. Добавьте метод, который принимает в качестве аргументов длину
#  и ширину одного рулона, а возвращает количество необходимых, исходя из оклеиваемой площади.
# Разработайте интерфейс программы. Пусть она запрашивает у пользователя данные и выдает
#  ему площадь оклеиваемой поверхности и количество необходимых рулонов.


class Windoor:
    def __init__(self, w, h):
        self.square = w * h


class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []

    def ad_wd(self, w, h):
        self.wd.append(Windoor(w, h))

    def brutto_walls_square(self, x, y, z):
        self.square = 2 * z * (x + y)

    def netto_walls_square(self):
        netto_square = self.square
        for i in self.wd:
            netto_square -= i.square
        return netto_square

    def quantity_rul_wallpapers(self, rul_w, rul_h):
        rul_quant = (self.netto_square // (rul_w * rul_h)) + 1
        return rul_quant


# user interface
room_quant = int(input("Please enter how many rooms are? :"))

for i in range(room_quant):
    x = input(f"Please enter room{i+1} width:")
    y = input(f"Please enter room{i+1} length: ")
    z = input(f"Please enter room{i+1} height: ")
    room = Room(x, y, z)
    win_quant = int(input("Please enter how many windows are? :"))
    for i in range(win_quant):
        w = input(f"Please enter room{i+1} width:")
        h = input(f"Please enter room{i+1} height: ")
        room.ad_wd(w, h)
    room.netto_walls_square()


# room1 = Room(10, 5, 3)
# room1.ad_wd(1, 1)
# room1.ad_wd(2, 1)

# print(room1.netto_walls_square())


# 3
import math


class Windoor:
    def __init__(self, w, h):
        self.square = w * h


class Room:
    def __init__(self, width, lenght, height):
        self.width = width
        self.lenght = lenght
        self.height = height
        self.wd = []

    def full_surface(self):
        self.square = 2 * self.height * (self.width + self.lenght)
        return self.square

    def wd_append(self, w, h):
        self.wd.append(Windoor(w, h))
        return self.wd

    def netto_walls_square(self):
        netto_square = self.full_surface()
        for i in self.wd:
            netto_square -= i.square
        return netto_square

    def walpapers(self, l, w):
        rulon_quant = math.ceil(self.netto_walls_square() / (l * w))
        return rulon_quant


room1 = Room(6, 5, 3)
room1.wd_append(1, 2)
room1.wd_append(1, 1)


print(room1.netto_walls_square())
print(room1.walpapers(1, 15))
