# Write a function that takes a datetime object, which will represent employees starting
# work day. and will return amount of total holidays gained during the work until today.
# 1 Month = 1.6 day off

import datetime

y = datetime.datetime.today()
today_str = y.strftime("%Y %m %d")
today_datetime = datetime.datetime.strptime(today_str, "%Y %m %d")
# print(type(today_datetime))

working_first_day = datetime.datetime(2022, 4, 11)
# print(type(working_first_day))


def gained_holiday_days(working_first_day):
    difference = today_datetime - working_first_day
    month = difference.days / 30
    holliday_days = month * 1.6
    print(int(holliday_days))


gained_holiday_days(working_first_day)
