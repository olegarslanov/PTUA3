# Create a class method to return the factorial of a given number.


class MyClass:
    @classmethod
    def factorial(cls, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * cls.factorial(n - 1)


print(MyClass.factorial(5))


# 2 instance metodu
# class MyClass:
#     def __init__(self, n):
#         self.n = n

#     def factorial(self, n: int) -> int:
#         if n == 0:
#             return 1
#         else:
#             return n * self.factorial(n - 1)


# fact1 = MyClass(5)
# print(fact1.factorial(5))
