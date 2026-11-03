import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

#load the data 
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#display the first few rows of the dataset
print(df.info())

#preview the first few rows of the dataset
print(df.head())

#apply one hot encoding
df_one_hot = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
print(df_one_hot.head())

#apply label encoding
label = LabelEncoder()
df['Pclass_encoded'] =  label.fit_transform(df['Pclass']) 

#display the first few rows of the dataset after encoding
print("\n label encoded dataset:")
print(df[['Pclass_encoded','Pclass']].head())


#apply frequency encoding
df['Ticket_freq'] = df.groupby('Ticket')['Ticket'].transform('count')
print("\n frequency encoded dataset:")
print(df[['Ticket_freq','Ticket']].head())