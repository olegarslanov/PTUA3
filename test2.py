class Calc:
    MY_NUMBER = 2

    def __init__(self, nr: int) -> None:
        self.MY_NUMBER += nr


cal_one = Calc(nr=3)

print(cal_one.MY_NUMBER)
print(cal_one())
