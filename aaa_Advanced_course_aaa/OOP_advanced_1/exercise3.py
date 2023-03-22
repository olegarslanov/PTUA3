# Define the Animal, Mammal, and Primate classes.
# Animal should have a name attribute and a make_noise() method.
# Mammal should have a warm_blooded attribute and a give_birth() method.
# Primate should have an opposable_thumbs attribute and a swing() method.
# Test the classes by creating a Chimpanzee and making it do various things :) 🐒


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_noise(self):
        print(
            f"When 'U ha ha ha-a-a': shout {self.name} ... then 'r-r-r-r...' : roared Lion, 'uhu uhu-u-u ...' shout Philline ...."
        )


class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool) -> None:
        self.warm_blooded = warm_blooded
        super().__init__(name)

    def give_birth(self):
        print(
            f"{self.warm_blooded} born small creature, which always want suck mother chest"
        )


class Primate(Mammal):
    def __init__(self, name: str, warm_blooded: bool, opposable_thumbs: bool) -> None:
        self.oppasable_thumbs = opposable_thumbs
        super().__init__(name, warm_blooded)

    def get_swing(self):
        print(f"{self.name} swing branches on palma")


Chimpanzee = Primate("chimpanzee", True, True)

Chimpanzee.get_swing()
Chimpanzee.give_birth()
Chimpanzee.make_noise()
