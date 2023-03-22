# i) Define a simple class called Individual.
# ii) Add an initialisation method which initialises the self.character_name instance
# attribute.
# iii) Add an access method to the class that returns self.character_name. Call this method
# get_character_name().
# iv) Create an instance of the character class and assign it to the variable individual1. This
# class instance should be assigned the character_name ‘Buster’ on initialisation.
# v) Create another instance, which should be assigned to the variable individual2. Set the
# name to ‘Tobias’.
# vi) Print the character name of individual1 and individual2 to the screen using the
# appropriate method.


class Individual:
    def __init__(self, character_name):
        self.character_name = character_name

    def get_character_name(self):
        return self.character_name


individual1 = Individual("Buster")
individual2 = Individual("Tobias")

print(individual1.get_character_name())
print(individual2.get_character_name())
