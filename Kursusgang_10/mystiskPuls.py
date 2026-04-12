import numpy as np

def find_kmeans(X, k=2, max_itr=5):
    indices = np.random.choice(len(X), replace=False)
    centroids = X[indices]

    for i in range(max_itr):
        distances = np.linalg.norm(X[:, None] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(2)])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
        return labels, centroids

np.random.seed(0)
puls_maalinger = np.random.normal([95, 61, 99, 63, 58, 92, 67, 65])
samples = np.random.normal([1, 2, 3, 4, 5, 6, 7, 8])

# Afstanden i et 1D array er blot afstanden mellem tallene

X = np.vstack([puls_maalinger])

findKlusters = find_kmeans(X)

print(findKlusters)

# GENBESØG DENNE OPGAVE
# Feature arrays skal være 2D


