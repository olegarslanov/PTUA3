# Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:

# model: "Тойота"
# color: "Розовый"
# number: "П111УУ77"

# Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.


class Car:
    pass


print(Car.__dict__)

setattr(Car, "model", "Toyota")
setattr(Car, "color", "Pink")
setattr(Car, "number", "p111yy77")


print(Car.__dict__)

print(Car.model)

print(Car.color)
print(Car.__dict__["color"])
