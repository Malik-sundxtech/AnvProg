import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, confusion_matrix


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

print(f"Feature shape: {x.shape}") # Fortæller noget om formen af arrayet, dvs. hvor mange rækker og kolonner. dvs. der er 569 rækker og 2 kolonner(2 features) her
print(f"Labels shape: {y.shape}") 
print(f"Target names: {data_breast_cancer.target_names}") # Printer target names - targets(værdier i 0 og 1 alt efter om det er malignant eller bening, som er de to klustre der er)
print(f"Labels shape: {data_breast_cancer.feature_names[:2]}") # Printer de første 2 features

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print(f"Træningsdata feature shape: {x_train.shape}") 
print(f"Træningsdata labels shape: {y_train.shape}") 

#KNN

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Nøjagtighed er {acc:0.2f}")
print(f"Confusion matrix er: \n {cm}")

# Plot
"""
y værdierne er malignant og benign, dvs. hvis c(color) er farven som nok er en colorgrade mellem 0 og 1, dvs. den kan skifte farve alt efter hviken værdi y har
"""
plt.scatter(x_test[:,0], x_test[:,1], c=y_test, edgecolors="k", label="Test")
plt.scatter(x_train[:,0], x_train[:,1], c=y_train, marker="x", label="Train")
plt.xlabel(data_breast_cancer.feature_names[0])
plt.ylabel(data_breast_cancer.feature_names[1])
plt.legend()
plt.show()
