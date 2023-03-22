# i)Add a class attribute called self.Counter that records the number of Individual
# instances created. This should be incremented by a class method called AddOne(). This
# way we can keep track of the total number of individuals. The current count total should
# be assigned to the instance variable self.id on instantiation. 
# ii) Create __str__ and __repr__ methods to give a human-readable representation of each
# instance of individual. It should return: individual: [self.id self.character_name]
# iii) Write additional code to verify the class is working as expected.



class Individual:

    def __init__(self, character_name, happy=True):
        self.character_name = character_name
        self.happy = happy
    
    def get_character_name(self):
        return self.character_name

    def is_happy(self):
        return self.happy

    def switch_mood(self):
        self.happy = False
        return self.happy

    def speak(self):
        if self.happy == True:
            return f"Hello, I am {self.character_name}"
        else:
            return f"{self.character_name}: 'Go away!'"
    
    
    
    def add_one(self):



individual1 = Individual("Buster")
individual2 = Individual("Tobias")
individual3 = Individual("Lucille")

# print(individual1.get_character_name())

print(individual3.is_happy())
print(individual3.speak())
print(individual2.switch_mood())
print(individual2.speak())
