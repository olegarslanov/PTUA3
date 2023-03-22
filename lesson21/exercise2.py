# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.

#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.

#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5.
#     Round to two decimal places.

#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive 
#     sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". 
#     Remember to change "-berries" to "-berry". See the examples below.

# Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and 
# call all methods you implemented.




class Smoothie:
    
    def __init__(self):
        self.ingridients = {}
              

    def get_cost(self) -> float:
        
        cost = round(sum(self.ingridients.values()), 2)
        return cost
    

    def get_price (self) -> float:
        cost = self.get_cost()
        price = cost + cost * 1.5
        return price


    def get_name(self) -> str:
       
        sorted_keys = sorted(self.ingridients.keys())

        if len(sorted_keys) > 1:
            return "Fusion: " + "&".join(sorted_keys)
        else:
            return sorted_keys[0] + " Smoothie"
        



class BerryBanana(Smoothie):

    def __init__(self):
        super().__init__()
        self.ingridients = {"berry" : 0.50, "banana" : 0.30}


class KiwiMelon(Smoothie):

    def __init__(self):
        super().__init__()
        self.ingridients = {"kiwi" : 0.40, "melon" : 0.70}



berry_banana = BerryBanana()
kiwi_melon = KiwiMelon()




print(berry_banana.get_cost())

print(berry_banana.get_price())

print(berry_banana.get_name())



#2 

# class Smoothie:
    
#     def __init__(self, ingridients):
#         self.ingridients = ingridients
              

#     def get_cost(self) -> float:
        
#         cost = round(sum(self.ingridients.values()), 2)
#         return cost
    

#     def get_price (self) -> float:
#         cost = self.get_cost()
#         price = cost + cost * 1.5
#         return price


#     def get_name(self) -> str:
       
#         sorted_keys = sorted(self.ingridients.keys())

#         if len(sorted_keys) > 1:
#             return "Fusion: " + "&".join(sorted_keys)
#         else:
#             return sorted_keys[0] + " Smoothie"
        


# ingridients = {"berry" : 0.50, "banana" : 0.30}

# berry_banana = Smoothie(ingridients)



# print(berry_banana.get_cost())

# print(berry_banana.get_price())

# print(berry_banana.get_name())
