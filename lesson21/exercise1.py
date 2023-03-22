
# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate

# In this class, create the method taste():
#     It will take in a food name as a string.
#     Return {person_name} eats the {food_name}.

#     If the food is in the person's like list, add 'and loves it!' to the end.
#     If it is in the person's hate list, add 'and hates it!' to the end.
#     If it is in neither list, simply add an exclamation mark to the end.
    
    
#     p1 = Person("Sam", ["ice cream"], ["carrots"])
#     p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#     p1.taste("cheese") ➞ "Sam eats the cheese!"
#     p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"


from typing import List


class Person:

    def __init__(self, name:str, list_like: List[str], list_hate: List[str]) -> None:
        self.name = name
        self.list_like = list_like
        self.list_hate = list_hate


    def taste(self, food_name:str) -> str:

        if food_name in self.list_like:
            return f"{self.name} eats the {food_name} and loves it!"
        elif food_name in self.list_hate:
            return f"{self.name} eats the {food_name} and hates it!"
        else:
            return f"{self.name} eats the {food_name}"
        
        

p1 = Person(name = "Oleg", list_like = ["ice cream", "cake", "chocolate"], list_hate = ["carrots", "onions", "milk"])



print(p1.taste("cake"))

print(p1.taste("onions"))

print(p1.taste("butter"))

print(p1.name)


