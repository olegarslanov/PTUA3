

return_cents = float(input("Please enter change sum:"))



cents_toonie = 200
cents_loonie = 100
cents_quarter = 25
cents_ten = 10
cents_five = 5
cent_one = 1


return_cents_toonie = int(return_cents // cents_toonie)
print(return_cents_toonie, "toonie coin")
return_cents = return_cents % cents_toonie

return_cents_loonie = int(return_cents // cents_loonie)
print(return_cents_loonie, "loonie coin")
return_cents = return_cents % cents_loonie

return_cents_quarter = int(return_cents // cents_quarter)
print(return_cents_quarter, "coin of 25 cents")
return_cents = return_cents % cents_quarter

return_cents_ten = int(return_cents // cents_ten)
print(return_cents_ten, "coin of 10 cents")
return_cents = return_cents % cents_ten

return_cents_five = int(return_cents // cents_five)
print(return_cents_five, "coin of 5 cents")
return_cents = return_cents % cents_five

return_cents_one = int(return_cents // cent_one)
print(return_cents_one, "coin of 1 cent")
return_cents = return_cents % cent_one

