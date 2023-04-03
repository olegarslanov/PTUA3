
BASE = 2400

employee_reiting = float(input("Please enter reiting coef.:"))


if employee_reiting == 0.0:
    alga = BASE * 0.0
    print("low level") 
elif employee_reiting == 0.4:
    alga = BASE * 0.4
    print("middle level") 
elif employee_reiting >= 0.6:
    alga = BASE * employee_reiting
    print("high level")
else:
    print("something wrong!")
    alga = 0

print(alga)








