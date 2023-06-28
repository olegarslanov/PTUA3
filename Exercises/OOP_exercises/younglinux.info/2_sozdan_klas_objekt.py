# Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два
# экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. В случайном порядке
# они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно
# уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение,
# какой юнит атаковал, и сколько у противника осталось здоровья. Как только у кого-то
# заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.


# from random import randint


# class Soldier:
#     def make_health(self, value):
#         self.health = value

#     def make_damage(self, enemy):
#         enemy.health -= 20


# voin_Terem = Soldier()
# voin_Terem.make_health(100)

# voin_Zajac = Soldier()
# voin_Zajac.make_health(100)


# while voin_Terem.health > 0 and voin_Zajac.health > 0:
#     c = randint(1, 2)
#     if c == 1:
#         voin_Terem.make_damage(voin_Zajac)
#         print(f"Atakoval voin_Terem, u voin_Zajac ostalos zdorovja {voin_Zajac.health}")

#     elif c == 2:
#         voin_Zajac.make_damage(voin_Terem)
#         print(f"Atakoval voin_Zajac, u voin_Terem ostalos zdorovja {voin_Terem.health}")


# if voin_Terem.health > voin_Zajac.health:
#     print("Pobedil voin Terem")
# else:
#     print("Pobedil voin Zajac")


# 2
from random import randint


class Soldier:
    health = 100

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= 20
        print(self.name, "бьет", enemy.name)
        print("%s = %d" % (enemy.name, enemy.health))


class Battle:
    result = "Сражения не было"

    def battle(self, u1, u2):
        while u1.health > 0 and u2.health > 0:
            n = randint(1, 2)
            if n == 1:
                u1.make_kick(u2)
            else:
                u2.make_kick(u1)
        if u1.health > u2.health:
            self.result = u1.name + " ПОБЕДИЛ"
        elif u2.health > u1.health:
            self.result = u2.name + " ПОБЕДИЛ"

    def who_win(self):
        print(self.result)


first = Soldier()
second = Soldier()
first.set_name("AAA")
second.set_name("BBB")

b = Battle()
b.battle(first, second)
b.who_win()
