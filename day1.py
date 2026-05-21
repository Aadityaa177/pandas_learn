#first Comment
import pandas as pd
print(pd.__version__)

L = [True,False]

ser = pd.Series(L,index=["a","b"])

print(ser)
