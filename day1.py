#first Comment
import pandas as pd
print(pd.__version__)

L = [100,102, 104, 200, 202]

ser = pd.Series(L,index=["a","b","c","d","e"])

print(ser[ser>=200])


