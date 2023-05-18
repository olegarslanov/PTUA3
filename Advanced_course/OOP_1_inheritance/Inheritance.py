# class Vehicle:
#     def __init__(self, name: str) -> None:
#         self.name: str = name
#     def get_name(self) ->  str:
#         return self.name# class Engine:
#     def __init__(self, name: str) -> None:
#         self.name = name
#     def say_hi_engine(self) -> None:
#         print(f'Hi engine with name {self.name}')
# class Golfiukas(Vehicle, Engine):
#     def __init__(self, name: str, cost: float) -> None:
#         super().__init__(name=name)
#         Engine.__init__(self, name=name)
#         self.cost: float = cost
#     def get_cost(self) -> float:
#         return self.cost
# CAR_NAME = 'Achujiena tacka'
# my_car = Golfiukas(name=CAR_NAME, cost=100)
# print(my_car.say_hi_engine())class Vehicle:
    def __init__(self):
        self.foobar = None    def foo(self) -> None:
        print("A.foo")
    def whatever(self) -> None:
        pass# class B(A):
#     def foo(self) -> None:
# #         print("B.foo")
# #     def foobar(self) -> None:
# #         print("B.foobar")
# # class C(A):#     def foo(self) -> None:
# #         print("C.foo")# class D(C, B):
# #     pass# d = D()
# # d.foo()  
# # prints "B.foo"
# # print(D.__mro__)
# # foo arba foobar, foorbar
# # class B: 
# #     def __init__(self):
# #         self.my_vehicle = Vehicle()
# #         self.my_vehicle.foo()
# #         print(self.my_vehicle.foobar)
# #         self another_class= AnotherClass(vehicle=self.my_vehicle)
# # class AnotherClass:
# #     def __init__(self, my_vehicle: Vehicle):
# #         self.my_vehicle = my_vehicle
# #     def foo(self) -> None:
# #         self.my_vehicle.whatever()class A:
    def foo(self) -> None:
        print("A.foo")
class B(A):
    def bar(self) -> None:
        print("B.bar")
class C(B):
    def baz(self) -> None:
        print("C.baz")
c = C()
c.foo()  # prints "A.foo"c.bar()  # prints "B.bar"c.baz()  
# prints "C.baz"class A: 
    '''    Methods to get the data from physical interface    '''    
    def read(self) -> None:
        passclass 
        
    PowerMeterSLXX522(A):
    def __init__(self) -> None:
        pass    def get_measurements(self) -> None:
        # Doing some stuff        some_binary_data = self.read()
        # Doing some stuff with that dataclass PowerMeter(PowerMeterSLXX522):
    def __init__(self) -> None:
        pass    
    def get_board_power(self) -> float:
        data = self.get_measurements()
        # doing some calc to get power valueclass Main:
    def __init__(self) -> None:
        self.power_meter = PowerMeter()
    def check_loop(self) -> None:
        do_stop = False        
        while not do_stop:
            if not self.power_meter.get_board_power():
                do_stop = True        
                # implement exit startegy