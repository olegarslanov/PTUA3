# Create a class called Employee with a static method called calculate_payroll that
#  takes a list of Employee instances and returns the total amount to be paid to all
#  employees. Each Employee instance has two attributes: name and salary.

from typing import List

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary: float = salary

    @staticmethod
    def calculate_payroll(employee_list: List["Employee"]) -> float:
        return sum(employee.salary for employee in employees_list)


employee_list = [Employee(name="Antanas", salary=1000), Employee(name="Vytautas", salary=2000, Employee(name="Oleg", salary=3000))]

print(Employee.calculate_payroll(employees_list=employee_list))