import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage


# 1. Load Seeds dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt"

data = pd.read_csv(url, sep=r"\s+", header=None)

print("First 5 rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)


# 2. Select first 7 columns as features
X = data.iloc[:, :7]

# Scale the data
X = StandardScaler().fit_transform(X)


# 3. K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

k_labels = kmeans.fit_predict(X)

print("\nK-Means")
print("Iterations:", kmeans.n_iter_)
print("Silhouette Score:", silhouette_score(X, k_labels))


# 4. Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=3, linkage="ward")

h_labels = hc.fit_predict(X)

print("\nHierarchical Clustering")
print("Silhouette Score:", silhouette_score(X, h_labels))


# 5. Compare
k_score = silhouette_score(X, k_labels)
h_score = silhouette_score(X, h_labels)

if k_score > h_score:
    print("\nK-Means gives better clustering.")
else:
    print("\nHierarchical Clustering gives better clustering.")


# 6. K-Means Graph
plt.figure(figsize=(8, 6))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=k_labels
)

plt.title("K-Means Clustering")
plt.xlabel("Area")
plt.ylabel("Perimeter")
plt.show()


# 7. Hierarchical Clustering Graph
plt.figure(figsize=(8, 6))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=h_labels
)

plt.title("Hierarchical Clustering")
plt.xlabel("Area")
plt.ylabel("Perimeter")
plt.show()


# 8. Dendrogram
plt.figure(figsize=(10, 6))

linked = linkage(X, method="ward")

dendrogram(
    linked,
    truncate_mode="lastp",
    p=30
)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()