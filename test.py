class Point:
    color = "red"
    circle = 2


Point.color = "black"
Point.circle

a = Point()
b = Point()

print(Point.__dict__)
print(a.__dict__)

a.color = "green"

print(a.__dict__)
