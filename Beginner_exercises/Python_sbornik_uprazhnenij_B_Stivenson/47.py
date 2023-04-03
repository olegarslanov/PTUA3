# import datetime


month = input("Please enter month:")

day = int(input("Please enter day:"))



if month in ("januar", "februar"):
    season = "Winter"
elif month in ("april", "may"):
    season = "Spring"
elif month in ("jule", "august"):
    season = "Summer"
elif month in ("october", "november"):
    season = "Autumn"


if (month =="december") and (day <= 20):
    season = "Autumn"
elif (month == "december") and (day > 20):
    season = "Winter"

elif (month == "march") and (day >= 20):
    season = "Spring"
elif (month == "march") and (day < 20):
    season = "Winter"

elif (month == "june") and (day >= 21):
    season = "Summer"
elif (month == "june") and (day < 21):
    season = "Spring"


elif (month == "september") and (day >= 22):
    season = "Autumn"
elif (month == "september") and (day < 22):
    season = "Summer"


print(season)