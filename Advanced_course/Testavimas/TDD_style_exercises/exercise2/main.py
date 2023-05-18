# implement program using TDD: Fizz buzz is a group word game for children to teach them
#  about division. Players take turns to count incrementally, replacing any number divisible
# by three with the word "fizz", and any number divisible by five with the word "buzz", and
#  any number divisible by both 3 and 5 with the word "fizzbuzz".


def convert_int_to_fizz(any_number):
    if any_number % 3 == 0:
        return "fizz"


def convert_int_to_buzz(any_number):
    if any_number % 5 == 0:
        return "buzz"


def convert_int_to_fizzbuzz(any_number):
    if any_number % 3 == 0 and any_number % 5 == 0:
        return "fizzbuzz"


any_number = 12
convert_int_to_fizz(any_number)
convert_int_to_buzz(any_number)
convert_int_to_fizzbuzz(any_number)
