import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sk

file = "/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_3/files/peaks_ECGPCG2.csv"

R, S1, S2 = np.genfromtxt(file, delimiter=",", unpack=True, skip_header=1)

RR = np.diff(R)

RR_mean = np.mean(RR)
RR_std = np.std(RR)


plt.scatter(["Baseline"]*len(RR), RR)
plt.errorbar(["Baseline"], RR_mean, 2*RR_std)

plt.show()