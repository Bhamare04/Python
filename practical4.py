# ============================================================
# Implement Naïve Bayes and K-Nearest Neighbor Classifier
# on Social Network Ads Dataset
# Compare Accuracy and Precision
# ============================================================


# -----------------------------
# 1. Import Libraries
# -----------------------------

import pandas as pd
import numpy as np
import os
import kagglehub

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix


# -----------------------------
# 2. Download Dataset
# -----------------------------

path = kagglehub.dataset_download("shub99/social-network-ads")

print("Dataset downloaded to:")
print(path)


# -----------------------------
# 3. Load Dataset
# -----------------------------

csv_path = os.path.join(path, "Social_Network_Ads.csv")

data = pd.read_csv(csv_path)

print("\nFirst 5 rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)


# -----------------------------
# 4. Select Features and Target
# -----------------------------

# Input features
X = data[['Age', 'EstimatedSalary']]

# Target variable
y = data['Purchased']


# -----------------------------
# 5. Split Dataset
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\nTraining data:", X_train.shape)
print("Testing data :", X_test.shape)


# -----------------------------
# 6. Feature Scaling
# -----------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ============================================================
# 7. NAÏVE BAYES CLASSIFIER
# ============================================================

nb = GaussianNB()

# Train model
nb.fit(X_train_scaled, y_train)

# Prediction
y_pred_nb = nb.predict(X_test_scaled)


# Calculate Accuracy
accuracy_nb = accuracy_score(y_test, y_pred_nb)

# Calculate Precision
precision_nb = precision_score(y_test, y_pred_nb)


print("\n================================")
print("       NAÏVE BAYES RESULTS")
print("================================")

print("Accuracy :", accuracy_nb)
print("Precision:", precision_nb)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_nb))


# ============================================================
# 8. K-NEAREST NEIGHBOR CLASSIFIER
# ============================================================

# Create KNN model
knn = KNeighborsClassifier(n_neighbors=5)

# Train model
knn.fit(X_train_scaled, y_train)

# Prediction
y_pred_knn = knn.predict(X_test_scaled)


# Calculate Accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)

# Calculate Precision
precision_knn = precision_score(y_test, y_pred_knn)


print("\n================================")
print("      K-NEAREST NEIGHBOR")
print("================================")

print("Accuracy :", accuracy_knn)
print("Precision:", precision_knn)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_knn))


# ============================================================
# 9. COMPARE BOTH MODELS
# ============================================================

results = pd.DataFrame({

    "Model": [
        "Naïve Bayes",
        "K-Nearest Neighbor"
    ],

    "Accuracy": [
        accuracy_nb,
        accuracy_knn
    ],

    "Precision": [
        precision_nb,
        precision_knn
    ]
})


print("\n================================")
print("        MODEL COMPARISON")
print("================================")

print(results)


# ============================================================
# 10. Determine Best Model
# ============================================================

if accuracy_nb > accuracy_knn:
    print("\nBest Model based on Accuracy: Naïve Bayes")
elif accuracy_knn > accuracy_nb:
    print("\nBest Model based on Accuracy: KNN")
else:
    print("\nBoth models have the same Accuracy.")


if precision_nb > precision_knn:
    print("Best Model based on Precision: Naïve Bayes")
elif precision_knn > precision_nb:
    print("Best Model based on Precision: KNN")
else:
    print("Both models have the same Precision.")