# В Python класс (class) - это шаблон или описание объекта, который может содержать
# свойства и методы, которые могут быть использованы для создания экземпляров этого
# объекта. Классы позволяют создавать собственные типы данных и определять свойства
# и методы, которые могут быть использованы для управления и изменения состояния объектов.

# Классы могут иметь свойства (атрибуты) и методы. Атрибуты - это переменные, которые
# содержат данные, связанные с объектом, а методы - это функции, которые определены в
# классе и могут использоваться для взаимодействия с объектом и изменения его состояния.

# Классы в Python создаются с помощью ключевого слова "class", за которым следует имя
# класса. Например, класс "Person" может быть определен следующим образом:

# Example:
# Copy code
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# В этом примере класс "Person" имеет два атрибута - "name" и "age", и один метод - 
# "say_hello()", который выводит приветствие и информацию о персоне.

# Чтобы создать экземпляр класса, нужно вызвать его конструктор (метод "init()") и 
# передать нужные параметры. Например, следующий код создает экземпляр класса "Person":

# Example:
# person = Person("Alice", 25)
# person.say_hello() # выводит "Hello, my name is Alice and I am 25 years old."

# Таким образом, классы в Python позволяют определять собственные типы данных и 
# поведение объектов, основываясь на определенных в них методах и свойствах.


# self - taikom butent sita zodi prie objektinio programavimo, kadangi turi buti
# tvarkingai pagal pep specifikacijas priimta 


#1
from datetime import date
import datetime

class Person:
    description: str = "A simple normal human being"

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
    
    def greet(self):
        return f"Hello my name is {self.name}"
    
    def coming_now(self):
        return f"{self.name} is coming now ..."
    
    def calculate_days_left_till_black_friday(self):
        # get todays date
        # initialize black friday date
        # return black_friday_date - todays_date
        today = date.today()
        black_friday_date = datetime.date(2023, 11, 24)
        print(today)
        print(type(today))
        print(black_friday_date)
        print(type(black_friday_date))
        delta = black_friday_date - today
        return delta.days
    
    def get_eye_color(self, eye_color: str = "Brown") -> str:
        return eye_color


person1 = Person("Oleg", "Arslanov", 44)
person2 = Person("Leon", "Leonov", 75)


print(Person.description)

print(person1.greet())

print(person1.coming_now())

print(person2.name + " " + person2.surname)

print(person1.get_eye_color("Blue"))

print(person1.calculate_days_left_till_black_friday())


#2
class Item:
    def __init__(self, name:str, price: float, quantity=0):

        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!" 

        #Assign to self object        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())


#3
class Employee:
    koef = 1.04
    emps = 0

    def __init__(self, name, surname, sallary):
        self.name = name
        self.surname = surname
        self.sallary = sallary
      
        Employee.emps += 1
     
    def emailas (self):
        return self.surname + self.name + "@company.com"
    
    def surnames(self):
        return self.surname
    
    def koef_sallary(self):
        return self.sallary * Employee.koef
    
    def koef_sallary1(self):
        return self.sallary * koef
    

koef = 1.05

emp1 = Employee("Oleg" , "Arslanov", 60000)

emp2 = Employee("Tomas", "Test", 50000)


print(emp1.emailas())

print(emp1.surnames())
print(Employee.surnames(emp1))

print(emp1.koef_sallary())
print(emp1.koef_sallary1())

print(Employee.emps)