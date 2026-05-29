import pandas as pd

df = pd.read_csv("pokemon.csv", index_col = "No")

# selection by rows
print(df.loc[25])
