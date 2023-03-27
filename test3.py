# Create an abstract class Money which takes currency and value as input and initializes it.

# A class must have these methods:
# get_value method which returns the value of the money.
# get_currency method which returns the currency of the money.
# convert_to_currency abstract method, which takes target currency and conversion rate as input
# and converts the value of the money to the target currency.

# Now create two subclasses of Money: Cash and Card. The Cash class should take the denomination
# of the cash as input in the constructor, and should implement the convert_to_currency method.

# The Card class should take the credit limit of the card as input in the constructor, and
# should implement the convert_to_currency method using the conversion rate to convert the
# value of the card to the target currency.


from abc import ABC, abstractmethod
from typing import Dict


class Money(ABC):
    def __init__(self, currency: str, value: float):
        self.currency = currency
        self.value = value

    def get_value(self) -> float:
        return self.value

    def get_currency(self) -> str:
        return self.currency

    @abstractmethod
    def convert_to_currency(
        self, target_currency: str, conversion_rate: Dict[str, float]
    ) -> None:
        pass


class Cash(Money):
    def __init__(self, currency: str, value: float, denomination: float):
        super().__init__(currency, value)
        self.denomination = denomination

    def convert_to_currency(self) -> None:
        self.value = self.denomination * (self.value // self.denomination)
        self.value = (
            self.value
            * conversion_rate[target_currency]
            * conversion_rate[self.currency]
        )
        self.currency = target_currency


class Card(Money):
    pass


conversion_rate = {
    "eur": 1.0,
    "dollar": 0.8,
    "rub": 60,
}


# cash1 = Cash("eur", 100, 3)

# print(cash1.convert_to_currency())


cash = Cash("dollar", 102, 5)
cash.convert_to_currency("rub", conversion_rate)
print(cash.get_currency(), cash.get_value())
