# Create a class called TimeUtils that has a static method called time_to_seconds that takes
#  a time string in the format hh:mm:ss and returns the total number of seconds represented
#  by that time. Use functional programing paradigm.

import time

current = time.localtime(time.time())
time_string = time.strftime("%H:%M:%S", current)
print(time_string)


class TimeUtils:
    @staticmethod
    def time_to_seconds(time_string: str) -> int:
        hour, minute, second = map(int, time_string.split(":"))
        seconds_sum = hour * 60 * 60 + minute * 60 + second
        return seconds_sum


print(TimeUtils.time_to_seconds(time_string))

# 2


class TimeUtils:
    @staticmethod
    def time_to_seconds(time_string: str) -> int:
        lst = list(map(int, time_string.split(":")))
        seconds_sum = lst[0] * 60 * 60 + lst[1] * 60 + lst[2]
        return seconds_sum


print(TimeUtils.time_to_seconds(time_string))
