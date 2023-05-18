# Write a Temperature class that has a celsius property and a fahrenheit property. The
#  celsius property stores the temperature in Celsius, and the fahrenheit property stores
#  the temperature in Fahrenheit. The fahrenheit property should be a computed property that
#  converts the Celsius temperature to Fahrenheit.


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        self._celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 1.8 + 32


temperature = Temperature(20)
print(temperature.fahrenheit)
