#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
# print(df.head(5))
# print(df.tail(5))
# print(df.info())
# print(df.describe())

selected_columns = df[['sepal_length', 'species']]
filtered = df[(df['species'] == 'setosa') & (df['sepal_length'] > 5.0)]

#print(filtered)

#create a dataframe with only the selected columns and filtered rows
result = selected_columns.loc[filtered.index]
# print(result)
# add a new column to the result dataframe
result['sepal_area'] = result['sepal_length'] * df.loc[filtered.index, 'sepal_width']
print(result)