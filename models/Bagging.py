#trains a bagging ensemble of decision trees on the training data and evaluates it on the test data
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score

# Load the iris dataset
X,y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a bagging classifier with decision trees as base estimators
bagging_model = BaggingClassifier( n_estimators=100, random_state=42)
bagging_model.fit(X_train, y_train)
# Make predictions
y_pred = bagging_model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

#params grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_samples': [0.5, 1.0],
    'max_features': [0.5, 1.0]
}
grid_search = GridSearchCV(estimator=bagging_model, param_grid=param_grid, cv=5, scoring='accuracy',n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best parameters found: ", grid_search.best_params_)
print("Best accuracy found: {:.2f}%".format(grid_search.best_score_ * 100))