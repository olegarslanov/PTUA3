order_amount = float(input("Please enter amount of Your order:"))

tips = 0.18
tips_amount = order_amount*tips

taxes = 0.21
taxes_amount = order_amount*taxes

total = order_amount+tips_amount+taxes_amount 

print("taxes = $%.2f, tips = $%.2f, total = $%.2f" %(taxes_amount, tips_amount, total))

