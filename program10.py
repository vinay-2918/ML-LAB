from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate data
X, y = make_blobs(n_samples=100, centers=3, random_state=42)

# Apply K-Means
model = KMeans(n_clusters=3)
model.fit(X)

# Plot clusters
plt.scatter(X[:,0], X[:,1], c=model.labels_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], color="red")
plt.show()
