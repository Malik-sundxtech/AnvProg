import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

data_glukose = np.array([171, 82, 118, 185, 78, 129, 165, 85, 178, 122]).reshape(-1,1) #Klustrer data

inertias = []
silhouette = []
ks = range(1, 5)

for k in ks:
    model = KMeans(n_clusters=k, random_state=0)
    model.fit(data_glukose)
    inertias.append(model.inertia_)
    if k > 1:
        silhouette.append(silhouette_score(data_glukose, model.labels_))
    else:
        silhouette.append(float("nan"))
    model.get_params()

plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.plot(ks, inertias, marker="o")
plt.title("Inertia")

plt.subplot(1,3,2)
plt.plot(ks, silhouette, marker="o")
plt.title("Silhouette")

plt.subplot(1,3,3)  
plt.scatter(data_glukose, [0]*len(data_glukose))
plt.title("Visualisering")

""" 
Lav lige denne opgave om også

"""
plt.show()