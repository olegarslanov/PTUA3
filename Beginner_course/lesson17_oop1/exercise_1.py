# Create a Calculator class with main functionality: add, divide, multiply,
# subtract , etc.. Initiate class and show up some calculations.


#1 su __init__
class Calculator:

    def __init__(self, calc, x, y):
        self.calc = calc
        self.x = x
        self.y = y


    def calc_add(self):
        return self.x + self.y
    def calc_sub(self):
        return self.x - self.y
    def calc_div(self):
        return self.x / self.y
    def calc_multi(self):
        return self.x * self.y



add = Calculator("addition", 100, 5)
sub = Calculator("Substaction", 100, 5)
div = Calculator("Division", 100, 5)
multi = Calculator("Multiplication", 100, 5)




print(add.calc_add())
print(sub.calc_sub())
print(div.calc_div())
print(multi.calc_multi())



#2 Supaprastinta
# class Calculator:
#     def add(self, x, y):
#         return x + y
#     def sub(self, x, y):
#         return x - y
#     def div(self, x, y):
#         return x / y
#     def multi(self, x, y):
#         return x * y


# calc = Calculator()

# calc.x = 100
# calc.y = 5


# print(calc.add(calc.x, calc.y))
# print(calc.sub(calc.x, calc.y))
# print(calc.div(calc.x, calc.y))
# print(calc.multi(calc.x, calc.y))


