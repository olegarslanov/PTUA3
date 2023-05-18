# Create a class which takes temperature measurements in Kelvins and add static methods
#  to transform those to Celsius and Fahrenheit units. Use OOP abstraction.

from abc import ABC, abstractmethod


class ConversionTool(ABC):
    CONSTANT = 273.15

    @abstractmethod
    def conversion_to_celsius(self):
        pass

    @abstractmethod
    def conversion_to_farenheit(self):
        pass


class Temperature(ConversionTool):
    @staticmethod
    def convert_to_celsius(kelvins: float) -> float:
        return f"Convert to celsius {round((kelvins - Temperature.CONSTANT), 2)}"

    @staticmethod
    def convert_to_farenheits(kelvins: float) -> float:
        return f"Conver to farenheit {round((kelvins - Temperature.CONSTANT) * (1.8 + 32), 2)}"


print(Temperature.convert_to_celsius(300))
print(Temperature.convert_to_farenheits(290))
