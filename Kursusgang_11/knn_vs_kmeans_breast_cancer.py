import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix


data_breast_cancer = load_breast_cancer()

# Find ud af hvilke data vi har
print(data_breast_cancer.keys())
print("\n")
print(data_breast_cancer.feature_names)
print("\n")
print(data_breast_cancer.target_names)


# Skal bruge de to første features mean radius og mean texture. Udtrækker dem
x = data_breast_cancer.data[:, 0:2] # Bruger kun de første to kolonner
y = data_breast_cancer.target

# Train data (splitter dataen)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
y_pred_knn = knn.predict(x_test)
acc_knn = accuracy_score(y_test, y_pred_knn)
rec_knn = recall_score(y_test, y_pred_knn)
cm_knn = confusion_matrix(y_test, y_pred_knn)

#Validering af KNN
print(f"Nøjagtighed er {acc_knn:0.2f}")
print(f"Recall er {rec_knn:0.2f}")
print(f"Confusion matrix er: \n {cm_knn}")

#KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(x_train)
y_pred_kmeans =kmeans.predict(x_test) # Skal predict de træningsdata jeg har ift. de test data jeg har

#Validering af KMeans
# Dette if statement skal anvendes før acc testes for KMeans, da det ikke er klassificeret
if np.sum(y_pred_kmeans == y_test) < np.sum(1 - y_pred_kmeans == y_test):
   y_pred_kmeans = 1 - y_pred_kmeans
   
acc_kmeans = accuracy_score(y_test, y_pred_kmeans)

# Plot
"""
y værdierne er malignant og benign, dvs. hvis c(color) er farven som nok er en colorgrade mellem 0 og 1, dvs. den kan skifte farve alt efter hviken værdi y har
plt.scatter(kmeans[:,0], kmeans[:,1])
"""
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(x_test[:,0], x_test[:,1], c=y_test, edgecolors="k", label="Test")
plt.scatter(x_train[:,0], x_train[:,1], c=y_train, marker="x", label="Train")
plt.xlabel(data_breast_cancer.feature_names[0])
plt.ylabel(data_breast_cancer.feature_names[1])

plt.subplot(1,2,2)
plt.scatter(kmeans[:,0], )
plt.xlabel(data_breast_cancer.feature_names[0])
plt.ylabel(data_breast_cancer.feature_names[1])


plt.legend()
plt.show()
