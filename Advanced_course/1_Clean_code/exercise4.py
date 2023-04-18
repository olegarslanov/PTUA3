# Magic Number problem. A number is said to be a magic number, if the sum of its digits are
#  calculated till a single digit recursively by adding the sum of the digits after every
#  addition. If the single digit comes out to be 1,then the number is a magic number.

# For example Number = 50113 => 5+0+1+1+3=10 => 1+0=1 This is a Magic Number
# For example Number = 1234 => 1+2+3+4=10 => 1+0=1 This is a Magic Number

# Write a python function that takes in one parameter - integer and then returns True if number
# is magic number or False if it is not a magic number


# # padariau is skaiciaus atskiru skaiciu lista
# user_number = input("Please enter number:")

# while int(user_number) > 9:
#     numbers_list = []
#     for number in str(user_number):
#         numbers_list.append(int(number))

#     user_number = sum(numbers_list)  # tiesiog susumuoju listo elementus tarpusavyje

# if user_number == 1:
#     return True
# else:
#     return False

# print(user_number)


def is_magic_number(num: int) -> bool:
    while num > 9:
        sum_of_digits = 0
        for digit in str(num):
            sum_of_digits += int(digit)
        num = sum_of_digits
    return num == 1


print(is_magic_number(46))
print(is_magic_number(17))
print(is_magic_number(91))
print(is_magic_number(179))
print(is_magic_number(7))
print(is_magic_number(1234567899999999999999999999999999999999999999999999999))
print(is_magic_number(1234))
