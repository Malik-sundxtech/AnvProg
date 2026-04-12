import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Indlæs data
data = load_iris()
print(data.keys())
print(data.feature_names)
selected_features = [2,3]

# Skaler data
X = StandardScaler().fit_transform(data.data)


features = X[:,1]


print(X[:,1])

plt.figure(figsize=(10,10))
plt.subplot(1,4,1)
plt.plot(X[:,0], [0]*len(X))
plt.subplot(1,4,2)
plt.plot(X[:,1], [0]*len(X))
plt.subplot(1,4,3)
plt.plot(X[:,2], [0]*len(X))
plt.subplot(1,4,4)
plt.plot(X[:,3], [0]*len(X))

plt.show()