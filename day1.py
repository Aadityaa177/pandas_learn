import pandas as pd
print(pd.__version__)

calories = {"day1":1750, "day2":2100,"day3":1700}
#no need index paramenter here since we have key value pairs
ser = pd.Series(calories)

print(ser.loc["day2"])
