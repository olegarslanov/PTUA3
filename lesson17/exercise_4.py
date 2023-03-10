# A country can be said as being big if it is:

# Big in terms of population.
# Big in terms of area.

# Add to the Country class so that it contains the attribute is_big. Set it to True
#  if either criterea are met:

# Population is greater than 20 million.
# Area is larger than 3 million square km.

# Also, create a method which compares a country's population density to another country
#  object. Return a string in the following format:

# {country} has a {smaller / larger} population density than {other_country}
# 

# Examples:
# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)

# australia.is_big ➞ True
# andorra.is_big ➞ False
# andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"



class Country:

    def __init__(self, country_name:str, population:int, area:int) -> None:
        self.country_name = country_name
        self.population = population
        self.area = area

    def is_big(self):
        return self.population > 20000000 or self.area > 3000000

    def compare_pd(self, other):
        if self.population / self.area > other.population / other.area:
            return(f"{self.country_name} has a larger population density than {other.country_name}")
        else:
           return(f"{other.country_name} has a larger population density than {self.country_name}")


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big())
print(andorra.is_big())
print(andorra.compare_pd(australia))















