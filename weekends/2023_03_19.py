class Point:
    color = "red"
    circle = 2


a = Point()

print(a.circle)

# print(type(a))

Point.type_pt = "disc"


print(Point.circle)
print(Point.color)

delattr(Point, "color")

print(Point.color)
