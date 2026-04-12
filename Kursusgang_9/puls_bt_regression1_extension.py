import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

puls = [60, 65, 70, 75, 80, 85, 90, 95]
puls = np.array(puls).reshape(-1, 1)
sys_blodtryk = [70, 72, 75, 78, 80, 83, 85, 88]

linReg = LinearRegression()
linReg.fit(puls, sys_blodtryk)

a = linReg.coef_[0]
b = linReg.intercept_
sys_predict = linReg.predict(puls.reshape(-1,1))

r2_score = linReg.score(puls, sys_blodtryk) #Indsæt værdier her - se svarark

rmse = np.sqrt(np.mean(sys_blodtryk-sys_predict)**2)

residuals = sys_blodtryk - sys_predict
mean_residuals = np.mean(residuals)
std_residuals = np.std(residuals)

print("="*50)

print(f"RMSE(root mean square error): {rmse}\n")

print(f"Reisduals: {residuals}\n")

print(f"Forudsat blodtryk: {sys_predict}\n")

print(f"Mean Reisduals: {mean_residuals}\n")

print(f"Std Reisduals: {std_residuals}\n")

print("="*50)

# Plot 1 - linear regression
plt.subplot(2,2,1)
plt.scatter(puls,sys_blodtryk)
plt.plot(puls, sys_predict, label =f"R = {r2_score:0.2f}", color="red")
plt.legend()


# Plot 2 - residualer vs forudsagt
plt.subplot(2,2,2)
plt.scatter(sys_predict, residuals)
plt.axhline(y=0, color="red", linestyle="--", alpha=0.6)
plt.legend()



# plot 3 - Histogram af residualer
plt.subplot(2,2,3)
plt.hist(residuals)
plt.axvline(x=0, linestyle="--", color="red", alpha=0.6)
plt.legend()

plt.show()

""" Forklarende tekst:
Linear model: 

R^2: Denne værdi er 1, dvs. puls fortæller 100% omkring blodtrykket

Residualer omkring 0(tilfældigt eller mønster): Værdierne er tilfældige, hvilket er et godt tegn. 
Hvorimod hvis der var et mønster såsom sinuskurve, så vil vi konstant afvige fra den predicted værdi hvilket ikke er så godt

Histogrammer skal laves bins(tykkelsen af søjlerne) mindre for at det er nemmere at se. Skal gerne have en klokkeform over histogrammer


"""