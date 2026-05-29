import pandas as pd

df = pd.read_csv("pokemon.csv", index_col = "No")

# selection by rows
print(df.iloc[0:11,0:3])
