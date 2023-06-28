# Разработайте программу по следующему описанию.

# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
# номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод
# "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев
# есть метод увеличения собственного уровня.

# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются
# объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд
# добавляются в разные списки.

# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя,
# принадлежащего команде с более длинным списком, увеличивается уровень.

# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные
# номера этих двух юнитов.

from random import randint


class Person:
    count = 0

    def __init__(self, team):
        self.team = team
        self.id = Person.count
        Person.count += 1


class Soldier(Person):
    def __init__(self, team):
        Person.__init__(self, team)
        self.hero = None

    def follow(self, hero):
        self.hero = hero.id


class Hero(Person):
    def __init__(self, team):
        Person.__init__(self, team)
        self.level = 1

    def level_up(self):
        self.level += 1


h1 = Hero(1)
h2 = Hero(2)

team1 = []
team2 = []

for i in range(20):
    n = randint(1, 2)
    if n == 1:
        team1.append(Soldier(n))
    else:
        team2.append(Soldier(n))

print(len(team1), len(team2))

if len(team1) > len(team2):
    h1.level_up()
else:
    h2.level_up()

team1[0].follow(h1)

print(team1[0].id, h1.id)
