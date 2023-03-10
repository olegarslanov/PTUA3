# Create the instance attributes fullname and email in the Employee class. 
# Given a person's first and last names:

#      Form the fullname by simply joining the first and last name together, 
#      separated by a space.
#      Form the email by joining the first and last name together with a . in 
#      between, and follow it with @company.com at the end. Make sure the entire 
#      email is in lowercase.


class Employee:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
                
    def full_name(self):
        return self.name + " " + self.surname

    def email_ad(self):
        email = self.name + self.surname
        email = email.lower()
        email = ''.join((email, '@company.com'))
        email = "".join(("a.", email))
        return email



employee1 = Employee("Oleg", "Arslanov")
employee2 = Employee("Leon", "Leonas")
employee3 = Employee("Aleksej", "Golubkovas")


print(employee1.full_name())
print(employee1.email_ad())

print(employee3.full_name())
print(employee3.email_ad())








