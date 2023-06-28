# Напишите программу по следующему описанию:

# Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя,
# фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию,
# равное единице.

# У класса Person есть метод, который возвращает строку, включающую в себя всю информацию
# о сотруднике.

# Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
# (вместо троеточия должны выводиться имя и фамилия объекта).

# В основной ветке программы создайте три объекта класса Person. Посмотрите информацию о
# сотрудниках и увольте самое слабое звено.

# В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет
# нажат Enter. Иначе вы сразу увидите как удаляются все объекты при завершении работы программы.


class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def get_info(self):
        return "{} {}, {}".format(self.surname, self.name, self.qualification)

    def __del__(self):
        print(f"До свидания, мистер {self.name, self.surname}")


staff = [
    Person("Oleg", "Arslanov", 3),
    Person("Arijus", "Mikutovicius"),
    Person("Samanta", "Fox", 2),
]

for person in staff:
    print(person.get_info())

staff.sort(reverse=True, key=lambda p: p.qualification)
del staff[-1]

print("Konec programmy")
input()
