# Write a function that calculates difference in days between two datetimes.


import datetime

now = datetime.datetime.now()
past = datetime.datetime(1990, 3, 11)


def calculate_difference_days(now, past):
    diference = now - past
    print(diference.days)


calculate_difference_days(now, past)

# 2
# calculate_difference_days(datetime.datetime.now(), datetime.datetime(1990, 3, 11))
