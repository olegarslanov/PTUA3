
# Create a few examples of yourself where you show four pillars of OOP in action.


# inheritance example



class Building:
    def __init__(self, constr_type: str, use_type: str, life_cycle: int) -> None:
        self.constr_type = constr_type
        self.use_type = use_type
        self.life_cycle = life_cycle

    def get_constr_type(self) -> None:
        print(f'My building construction type: {self.constr_type}')

    def get_use_type(self) -> None:
        print(f'My building use type: {self.use_type}')

    def get_life_cycle(self) -> None:
        print(f'My building life cycle: {self.life_cycle}')


class Interior(Building):  
    def __init__(self, luxury_level:int, involvement_level:int, comunications:str) -> None:
        self.luxury_level = luxury_level
        self.involvement_level = involvement_level
        self.comunications = comunications

    def get_luxury_level(self) -> None:
        print(f'My building interrior : {self.luxury_level}')


class Exterior(Building):
    def __init__(self, facade_decoration: str, plot: int) -> None:
        self.facade_decoration = facade_decoration
        self.plot = plot
    
    def get_facade_decoration(self) -> None:
        print(f'Facade is {self.facade_decoration}')




buil_individ = Building("Reatining walls", "Individual", 80)
build_admin = Building("Frame", "Public", 100)

build_admin.get_constr_type()


interior = Interior("average", "0.8", "without gas")

interior.get_luxury_level()


# polymorphism

class T1:

    def __init__(self, n):
        self.n = n

    def total(self, a):
        return self.n + int(a)
    
class T2:
    def __init__(self, string):
        self.string = string
        
    def total(self, a):
        return len(self.string + str(a))
    
t1 = T1(10)
t2 = T2("Hello world")

print(t1.total(35))
print(t2.total(35))



# class T1:
#     def __init__(self):
#         self.n = 10
#     def total(self, a):
#         return self.n + int(a)
    
# class T2:
#     def __init__(self):
#         self.string = "Hi"
        
#     def total(self, a):
#         return len(self.string + str(a))
    
# t1 = T1()
# t2 = T2()

# print(t1.total(35))
# print(t2.total(35))


























































































