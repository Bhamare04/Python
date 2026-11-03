#train the gradient boosting model
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
#take the iris dataset and split it into training and testing sets
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
X,y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the gradient boosting model
fb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=42)
fb_model.fit(X_train, y_train)
y_pred = fb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Gradient Boosting Classifier Accuracy: {:.2f}%".format(accuracy * 100))
