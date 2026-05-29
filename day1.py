import pandas as pd

# aggregate - Reduces a set of values into a dingle summary value
#             Used to summarize and analyse data
#             Often used with the groupby() function
df = pd.read_csv("pokemon.csv", index_col = "Name")

print(df.mean(numeric_only=True))