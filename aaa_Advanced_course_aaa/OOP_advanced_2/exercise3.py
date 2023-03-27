# As per previous examples please create an example of your own. The abstract
# class should contain five (3 abstract and 2 normal ) methods. Create
# 2 subclasses that would inherit abstract class.


from abc import ABC, abstractmethod


class Estimate(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_add(self) -> float:
        pass

    @abstractmethod
    def get_total(self) -> float:
        pass

    def __init__(self, a, b) -> float:
        self.a = a
        self.b = b

    def get_substraction(self, a: float, b: float) -> float:
        return a - b
    
    def get_multiplication(self, a, b) -> float:
        return a * b

class materilas(Estimate):

    def get_name(self) -> str:

    def get_total(self) -> float:


class get_earning(Estimate):

    def get_name(self) -> str:

    def get_add(self) -> float:
        