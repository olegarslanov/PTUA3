class Purse:
    # def __init__(self):
    #     self.money = 0.00

    def info(self, money):
        self.money = money
        # return self.money


x = Purse()

print(x.info(100))


def save(self):
    with open("users") as r:
        for i in r:
            if f"{self.login, self.password}" + "\n" == i:
                raise ValueError("This one exists")
    Verification.save(self)
