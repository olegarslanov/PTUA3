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



# Lambda syntax:
lambda (<parameter_list> : <expression>)(<"paduodam kazka">)

# idedam parametra x, daro su (x, x**2, x**3) ("paduodam skaiciukus" (2))
# print((lambda x: (x, x**2, x**3))(2))


primes numbers:

n= 5
i= 1

while i in n:
    if i%2 == 0 or i%3 ==0:
        print(i, end = "")
    i+=1
