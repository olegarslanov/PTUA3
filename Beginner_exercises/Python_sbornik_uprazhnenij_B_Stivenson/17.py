




C = 4.186

m = (float(input("Enter gr of water:")))
T = (float(input("Enter heat ")))

q = m * C * T
print (q)

price = 0.30 

convert_to_kWh = q * 0.0000002778

price_total = convert_to_kWh * price

print(price_total )
