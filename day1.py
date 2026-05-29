import pandas as pd

df = pd.read_csv("pokemon.csv", index_col = "Name")

# Filtering : keeping the rows that match a condition

tall_pokemon = df[df["Height"]>=2]

heavy_pokemon = df[df["Weight"] > 100]

legendary = df[df["Legendary"]==1]

water_poke = df[(df["Type1"]=="Water")|(df["Type2"] == "Water")]

print(water_poke)
