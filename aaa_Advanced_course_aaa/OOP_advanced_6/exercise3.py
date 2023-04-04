# Create a class method to return the list of prime numbers up to a given number.


class Numbers:
    list_prime_numbers: list["Numbers"] = []

    def __init__(self, n):
        self.n = n
        Numbers.list_prime_numbers.append(self)

    @classmethod
    def get_list_prime_numb(cls) -> "Numbers":
        return (cls.list_prime_numbers, key=lambda )
    
        while number < n:
            print(number)
            number += 1


n: Numbers = Numbers (6)



# 2  loop metodu
# n = int(input())
# number = 1

# while number < n:
#     print(number)
#     number += 1
