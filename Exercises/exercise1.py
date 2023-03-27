# write a function that accepts a number as a parameter. The function should return a number
# that’s the difference between the largest and smallest numbers that the digits can form
# in the number.
# For example, if the parameter is “213”, the function should return “198”, which is the result
#  of 123 subtracted from 321.


number = input("Please enter number:")


def get_magic_number(number):
    number_quant = len(number)

    list_of_digits = [int(i) for i in str(number)]
    list_of_digits_max = []

    for _ in range(number_quant):
        list_of_digits_max.append(str(max(list_of_digits)))
        list_of_digits.remove(max(list_of_digits))

    list_of_digits = [int(i) for i in str(number)]
    list_of_digits_min = []

    for _ in range(number_quant):
        list_of_digits_min.append(str(min(list_of_digits)))
        list_of_digits.remove(min(list_of_digits))

    number_max = "".join(list_of_digits_max)
    number_min = "".join(list_of_digits_min)

    print(int(number_max) - int(number_min))


get_magic_number(number)


# 2
# number = input("Please enter 3-digit number:")


# def get_magic_number(number):
#     list_of_digits = [int(i) for i in str(number)]
#     max_numb, min_numb = max(list_of_digits), min(list_of_digits)
#     list_of_digits.remove(min_numb)
#     list_of_digits.remove(max_numb)
#     middle_numb = list_of_digits[0]

#     max_list = [max_numb, middle_numb, min_numb]
#     min_list = [min_numb, middle_numb, max_numb]

#     max1 = str(max_list[0]) + str(max_list[1]) + str(max_list[2])
#     min1 = str(min_list[0]) + str(min_list[1]) + str(min_list[2])

#     print(int(max1) - int(min1))


# get_magic_number(number)
