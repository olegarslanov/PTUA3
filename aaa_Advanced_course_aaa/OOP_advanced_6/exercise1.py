# Create a class method to return the factorial of a given number.


# class MyClass:
#     @classmethod
#     def factorial(cls, n: int) -> int:
#         if n == 0:
#             return 1
#         else:
#             return n * cls.factorial(n - 1)


# print(MyClass.factorial(5))


class MyClass:
    def __init__(self, n):
        self.n = n

    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


fact = MyClass(5)
# print(MyClass.factorial(fact))

print(fact.factorial())
