SQFT_PER_ACRE = 43560

length = int(input("Please enter plot length (ft):"))
width = int(input("Please enter plot width (ft):"))

area = length * width / SQFT_PER_ACRE

print("Plot square:", area, "acre")


