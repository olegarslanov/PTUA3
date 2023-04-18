def outer():
    def inner():
        print("I am function inner()!")

    return inner


function = outer()
print(function)
# <function outer.<locals>.inner at 0x7f18bc85faf0>
function()
# I am function inner()!

outer()()
# I am function inner()!


# Lambda syntax:
lambda (<parameter_list> : <expression>)(<"paduodam kazka">)

# idedam parametra x, daro su (x, x**2, x**3) ("paduodam skaiciukus" (2))
# print((lambda x: (x, x**2, x**3))(2))


print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, range(10))))
# [0, 2, 4, 6, 8]

print(list(filter(lambda x: x % 2 == 0, range(10))))
# [0, 2, 4, 6, 8]
