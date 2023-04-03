# Create a class Person that has two methods: set_name and set_age, which set the
# name and age attributes of the class, respectively. Modify these methods to return
# self, so that the calls can be chained together.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.adress = None

    def set_name(self, name: str) -> "Person":
        self.name = name
        return self

    def set_age(self, age: int) -> "Person":
        self.age = age
        return self

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


person1 = Person("Radomir", 6)
# person1.set_name().set_age()

print(person1)
