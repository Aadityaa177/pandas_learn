import pandas as pd

# aggregate - Reduces a set of values into a dingle summary value
#             Used to summarize and analyse data
#             Often used with the groupby() function
df = pd.read_csv("pokemon.csv", index_col = "Name")

#Whole data frame
#print(df.mean(numeric_only=True))

#print(df.sum(numeric_only=True))

#print(df.min(numeric_only=True))

#print(df.max(numeric_only=True))

#print(df.count())

# For single column

#print(df["Height"].mean())

#print(df["Height"].sum())

#print(df["Height"].min())

#print(df["Height"].max())

#print(df["Height"].count())

group = df.groupby("Type1")

print(group["Height"].mean())

print(group["Weight"].max())

