def convert_int_to_roman(number: int):
    dict = {
        1: ["I", 1],
        2: ["IV", 4],
        3: ["V", 5],
        4: ["IX", 9],
        5: ["X", 10],
        6: ["XL", 40],
        7: ["XC", 90],
        8: ["C", 100],
        9: ["CD", 400],
        10: ["D", 500],
        11: ["CM", 900],
        12: ["M", 1000],
    }

    i = 12

    answer = ""

    while number:
        div = number // dict[i][1]
        number %= dict[i][1]

        while div:
            answer += dict[i][0]
            div -= 1
        i -= 1
    return answer


# if __name__ == "__main__":
number = 3549
#     print f"Roman value:{answer}"
convert_int_to_roman(number)
