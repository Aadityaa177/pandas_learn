#first Comment
import pandas as pd
print(pd.__version__)

L = [100,102,103]

ser = pd.Series(L,index=["a","b","c"])



print(ser.loc["c"])
