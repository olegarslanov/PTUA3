big_bottles = float(input("Please enter amount of 1.0 ltr or more bottles:"))
small_bottles = float(input("Please enter amount of less than litr bottles:"))

big_bottle_price = 0.25
small_bottle_price = 0.10

refund = big_bottles*big_bottle_price + small_bottles*small_bottle_price


print("You got $%.2f." % refund)



