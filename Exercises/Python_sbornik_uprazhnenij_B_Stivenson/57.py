
min = int(input("Please enter total minutes:"))
sms = int(input("Please enter total sms:"))
     


if min <= 50:
    min_add = 0

elif min > 50:
    print("Papildomi skambuciai",(min-50))
    min_add = min-50
    min_add_price = float(min_add*0.25)


if sms <= 50:
    sms_add = 0

elif sms > 50:
    print("Papildomi sms",(sms-50))
    sms_add = sms-50
    sms_add_price = float(min_add*0.15)



plan = 15.00
print("Plan: $%.2f" %plan)

papildomai = 0
if (min_add + sms_add) > 0: 
    papildomai = min_add_price + sms_add_price
    print("Papildoma saskaita:", papildomai)

calling_centr = 0.44  

fee = (plan + papildomai + calling_centr) * 0.05

total = plan + papildomai + calling_centr + fee
          

print("Calling_centr: $%.2f " %calling_centr)

print("Fee: $%.2f " %fee)
print("Total: $%.2f " %total)