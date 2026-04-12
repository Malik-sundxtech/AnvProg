import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

file = "/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_3/files/features_table_b001.csv"

RR,R_amp,RtoS2,S1toS2,Resp_amp,Resp_amp_RR_mean,Resp__amp_RR_std = np.genfromtxt(file, skip_header=1, unpack=True, delimiter=",", autostrip=True, missing_values="", filling_values=np.nan)

mask = ~np.isnan(RR) & ~np.isnan(R_amp)

RR = RR[mask]
R_amp = R_amp[mask]

numerator = np.sum((RR-np.mean(RR)) * (R_amp- np.mean(R_amp)))
denominator = np.sum((RR-np.mean(RR))**2)
a = numerator/denominator

b_intersect = np.mean(R_amp) - a*np.mean(RR)

regressions_linje = a * RR  + b_intersect

print(a)
plt.scatter(RR, R_amp, label="Data")
plt.plot(RR, regressions_linje, color="red", zorder=2, label=f"{a:.2f} * RR  + {b_intersect:.2f}")
#plt.xlim(0,1)
#plt.ylim(0.5,2)


print(f"Ny forventet amplitude for RR=1.3 forventes at være: {(a * 1.3  + b_intersect):.2f} PPG")
"""
Slope: Amplituden stiger med 0.55 for hver gang RR stiger med 1
Intercept: Hvis RR = 0 ville amplituden være 0.63
"""
plt.legend()
plt.show()