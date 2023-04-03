import math



# (t1, g1) 
# (t2, g2)


latitude1 = float(input("Please enter latitude:"))
longitude1 = float(input("Please enter longitude:"))

latitude2 = float(input("Please enter latitude:"))
longitude2 = float(input("Please enter longitude:"))



t1 = math.radians(latitude1)
t2 = math.radians(latitude2)

g1 = math.radians(longitude1)
g2 = math.radians(longitude2)




distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print(distance)