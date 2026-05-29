import pandas as pd

df = pd.read_csv("pokemon.csv", index_col = "Name")

pokemon = input("Enter a Pokemon Name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")

