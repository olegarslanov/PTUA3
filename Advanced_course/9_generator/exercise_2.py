# Create a generator function that would pick word from a generator and/list of generated random
# words (should be > 10000) and would stop itterating until the word longer than 7 lettters is found.
# Compare sizes of list and generator. Calculate performance per both executions (time to
# complete in ms)

from random_word import RandomWords

# from collections.abc import Iterator


# def generate_words(n: int):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i


# my_generator = generate_even_numbers(5)

# for value in my_generator:
#     print(value)


n = 1
word = "start"

while n < 100 or len(word) > 7:
    r = RandomWords()
    word = r.get_random_word()
    print(word)
    n += 1
