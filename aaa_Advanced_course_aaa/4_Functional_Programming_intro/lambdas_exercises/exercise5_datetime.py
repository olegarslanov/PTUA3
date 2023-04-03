# Write a Python program to extract year, month, date and time using Lambda. Sample Output:
# 2020-01-15 09:03:32.744178 2020 1 15 09:03:32.744178


import time

current = time.localtime(time.time())
time_string = time.strftime("%H:%M:%S", current)
print(time_string)

import datetime

print((lambda x: x.year)(datetime.datetime.now()))


import datetime

print((lambda x: (x.hour, x.minute, x.second))(datetime.datetime.now()))


# 2
# Issirenku ka man reikia parrodyti
time = (lambda t: t.strftime("%H:%M"))(datetime.datetime.now())
print(time)
