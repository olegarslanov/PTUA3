
import math

a = float(input("Please input a:"))
b = float(input("Please input b:"))
c = float(input("Please input c:"))


# (a*(x**2)) + (b*x) + c = 0

diskriminant = b**2 - 4*a*c

if diskriminant < 0:
    print("roots number is 0")
elif diskriminant == 0:
    print("roots number is 1", (-b / 2*a))
else:
    print("roots number is 2", ((-b + math.sqrt(b**2 - 4*a*c)) / 2*a), ((-b - math.sqrt(b**2 - 4*a*c)) / 2*a))


