
#1

import calc as calculator

i = 20
y = 30

result = calculator.add(i,y)
print(result)

#2

from calc import *
a = 20
b = 30
 

if __name__ == "__main__":
    print(add(a,b))

    
# Uzrasas if __name__ == "__main__" kad duoti printuoti dali kodo, kuri yra po sio 
# uzraso tik esant sitame main lange (o ne kitame lange, kai mes importuojame 
# sita moduli i kita faila po uzrasu komandos nevykdys)


