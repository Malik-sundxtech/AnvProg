from operator import add
import numpy as np

a = 1
b = 2

c = a + b
print(c)


A = [1, 2]
B = [3, 4]
C = A + B

print(C)


C2 = list(map(add, A, B))
npA = np.array(A)
npB = np.array(B)
print(npA + npB)

# numpy addition is ~ 30x - 100x faster than map
