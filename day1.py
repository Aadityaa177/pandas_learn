import pandas as pd
print(pd.__version__)

#dataframe : A tabular data sttructure with rows and columns . (2 Dimensionals)
# similar to an excel spreadsheet

data = {"Name": ["Spongebob", "Patrick","Squidward"],
        "Age": [30,35,50]
        }

df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])

#Add a new column 
df["Job"] = ["Cook","N/A", "Casier"]

#Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job":"Doctor"}],index=["Employee 4"])
df = pd.concat([df,new_row])

print(df)