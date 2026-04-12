import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

LinReg = LinearRegression()

data_puls_sys = np.array([
    [74, 123], [61, 110], [88, 136], [69, 118], [95, 142], [57,106], [82, 129], [76, 124], [90, 138], [64, 113]
])

x = data_puls_sys[:, 0:1] #2D array
y = data_puls_sys[:, 1] #1D array

LinReg.fit(x, y)

a = LinReg.coef_[0] #0te koefficient
b = LinReg.intercept_

print(f"y = {a:0.2f} mmHg/puks + {b:0.2f} mmHg\n")


sys_predict = LinReg.predict([0], [88])


plt.plot(([0], [88]), sys_predict)
plt.scatter(x, y)
plt.show()


# GENBESØG DENNE OPGAVE