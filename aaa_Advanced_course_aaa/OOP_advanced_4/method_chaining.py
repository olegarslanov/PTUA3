class MyString:
    def __init__(self, value: str):
        self.value = value

    def add_exclamation(self) -> "MyString":
        self.value += "!"
        return self

    def make_upper(self) -> "MyString":
        self.value = self.value.upper()
        return self


my_string = MyString("hello")
my_string.add_exclamation().make_upper()

print(my_string.value)  # output: "HELLO!"


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.address = None

    def set_name(self, name: str) -> "Person":
        self.name = name
        return self

    def set_age(self, age: int) -> "Person":
        self.age = age
        return self

    def set_address(self, address: str) -> "Person":
        self.address = address
        return self

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.address}"


p = Person("John", 25)
p.set_address("123 Main St").set_age(26)

print(p)  # output: "John, 26, 123 Main St"
