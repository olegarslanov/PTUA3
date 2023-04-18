# Create a generator function that takes a positive integer n as input and generates all
# the even numbers up to and including n.


# 1
def generate_even_numbers():
    i = 1
    n = int(input())
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


my_generator = generate_even_numbers()

print(next(my_generator))
print(next(my_generator))

for value in my_generator:
    print(value)


# 2
# from collections.abc import Iterator


# def generate_even_numbers(n: int) -> Iterator[int]:
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i


# my_generator = generate_even_numbers(5)

# for value in my_generator:
#     print(value)
