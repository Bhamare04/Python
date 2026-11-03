#combinig the models

from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the iris dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create individual models
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=42)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Create a voting classifier
voting_model = VotingClassifier(estimators=[('gb', gb_model), ('rf', rf_model)], voting='hard')

# Train the voting classifier
voting_model.fit(X_train, y_train)

# Make predictions
y_pred = voting_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Voting Classifier Accuracy: {:.2f}%".format(accuracy * 100))