import pandas as pd

s = pd.Series([1,2,3], index=['a','b','c'])
print(s)

data = {"name" : ["Alice", "Bob", "Charlie"], "age" :[25,30,35]}
df  = pd.DataFrame(data)
print(df)
