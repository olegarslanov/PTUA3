# Let’s build on our individual class a little more to make it more interesting.
# i) On initialisation, set the instance attribute self.happy to True. This should be done by
# default (i.e. no parameter needs to be passed on instantiation in order to do this.)
# ii) Create a predicate method is_happy to return the status of self.happy.
# iii) Create a modification method named switch_mood()that changes self.happy from True
# to False (and vice versa).
# iv) Create a method called speak() that returns “Hello, I am [self.name]” or ‘Go away!’,
# depending
# on whether self.happy is set to True or False respectively.
# v) Create individual3 with character name initialised to ‘Lucille’
# vi) Write some code to try out these methods/attributes of Buster and Tobias.


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


individual1 = Individual("Buster")
individual2 = Individual("Tobias")
individual3 = Individual("Lucille")

# print(individual1.get_character_name())

print(individual3.is_happy())
print(individual3.speak())
print(individual2.switch_mood())
print(individual2.speak())
