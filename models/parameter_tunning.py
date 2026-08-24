from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score

#load the iris dataset
data = load_iris()
X,y =data.data,data.target

#split the dataset into training and testing sets
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#display the shape of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

print("feature names:", data.feature_names)
print("target names:", data.target_names)

#define the parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [ 50, 100, 200],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

#initi grid search with cross-validation

grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid,cv=5, n_jobs=-1, verbose=2)

#fit the grid search to the training data
grid_search.fit(X_train,y_train)

#display the best parameters and best score
print("Best parameters:", grid_search.best_params_)
print("Best cross-validation score:", grid_search.best_score_)

#make predictions on the test set
y_pred = grid_search.predict(X_test)

#display the classification report and accuracy score
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))