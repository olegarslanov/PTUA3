# Create an abstract class Animal with which takes name of animal as an input and
#  initialize it. The create speak abstract method, to be overridden by subclasses.
#  And get_name method which returns name of the animal.

# Now create two subclasses of Animals: Dog and Cat which overrides the speak method,
# and provide the implementation which returns a string "Dog says Woof!" and
# "Cat says Meow!" respectively.


# abstract

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        pass

    def get_name(self) -> str:
        return self.name


class Dog(Animal):
    def speak(self) -> str:
        return "Dog says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Cat says Meow!"


dog = Dog("Vaska")
print(dog.get_name())
print(dog.speak())

cat = Cat("Murka")
print(cat.speak())


# inheritance


# class Animal:
#     def __init__(self, name: str, speaking: str) -> None:
#         self.name = name
#         self.speaking = speaking

#     def speak(self) -> str:
#         return self.speaking

#     def get_name(self) -> str:
#         return self.name


# class Dog(Animal):
#     def __init__(self, name, speaking) -> None:
#         super().__init__(name, speaking)


# class Cat(Animal):
#     def __init__(self, name: str, speaking: str) -> None:
#         super().__init__(name, speaking)


# cat = Cat("Murka", "Cat says Meow")
# print(cat.get_name())
# print(cat.speak())

# dog = Dog("Vaska", "Dog says Woof")
# print(dog.get_name())
# print(dog.speak())
