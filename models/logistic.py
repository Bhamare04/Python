# Logistic Regression Implementation
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

# Generate synthetic data
np.random.seed(42)
n_samples = 100
X = np.random.rand(n_samples, 2)  # Two features
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Binary target variable

#create dataframe
import pandas as pd
df = pd.DataFrame(X, columns=['Age', 'Salary'])
df['Purchased'] = y

#split data
X_train, X_test, y_train, y_test = train_test_split(df[['Age', 'Salary']], df['Purchased'], test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

#make prediction
y_pred = model.predict(X_test)

#evaluate model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)
print("Classification Report:\n", report)

