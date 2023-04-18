class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def say_hello(self) -> None:
        print(f"hello, {self.name}")


person = Person("first", "person")
person.say_hello()


# Buvo:
# class person():
#     def __init__(self, name, surname):
#         self.name=name
#         self.surname=surname
#     def sayHello(self):
#         print(f"hello, {self.name}")
# PERSON = person("first", "person")
# PERSON.sayHello()
