import numpy as np

fruits = ["apple", "banana", "cherry"]
A = [5.0, 31.0, 6.0]
B = [1.0, 0.0, -66.0]


print(fruits)

fruits.remove("banana")

fruits.append("date")

for i in range(len(fruits)):
    print(f"{fruits[i]}")


print(f"{A+B=}") # Kombinerer A og B i forlængelse af hinanden

nA = np.array(A)
nB = np.array(B)
print(f"{nA+nB =}") # Lægger faktisk værdierne i array A og B sammen