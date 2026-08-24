import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#load titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#display the first few rows of the dataset
print(df.info())

#preview the first few rows of the dataset
print(df.head())

#select relevant features for scaling
df = df[['Pclass','Sex','Age','Fare','Embarked','Survived']]

#handle missing values
df.fillna({'Age': df['Age'].median()},inplace=True)
df.fillna({'Embarked': df['Embarked'].mode()[0]}, inplace=True)

#define features and target
X = df.drop(columns=['Survived'])
y = df['Survived']

#apply one hot encoding to categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Age', 'Fare']),
        ('cat', OneHotEncoder(drop='first'), ['Sex', 'Embarked'])
    ])

X_preprocessed = preprocessor.fit_transform(X)

#train and evaluate a logistic regression model
model = LogisticRegression()
log_scores = cross_val_score(model, X_preprocessed, y, cv=5,scoring='accuracy')

print("Logistic Regression Cross-Validation Scores:", f"{log_scores.mean():.2f}")

#train and evaluate a random forest classifier
rf_model = RandomForestClassifier()
rf_scores = cross_val_score(rf_model, X_preprocessed, y, cv=5,scoring='accuracy')
print("Random Forest Cross-Validation Scores:", f"{rf_scores.mean():.2f}")


#define hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    
}

#PERFORM GRID SEARCH
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42), param_grid=param_grid, cv=5, scoring='accuracy',n_jobs=-1)
grid_search.fit(X_preprocessed, y)

print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", f"{grid_search.best_score_:.2f}")
