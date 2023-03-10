acount_money = float(input("Please input acount amount:"))

procents_stavka = 0.04
count = 0
metu = 3

acount_money_proc =[]

while count in range(metu):
    acount_money = acount_money + acount_money*procents_stavka
    print(round(acount_money,2))
    count +=1
    



