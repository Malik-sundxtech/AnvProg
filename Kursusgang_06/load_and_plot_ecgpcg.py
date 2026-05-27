import numpy as np
import matplotlib.pyplot as plt


file = "/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_2/files/ECGPCG.csv"

timestamps, ECG, PCG = np.genfromtxt(file, unpack=True, usecols={0,1,2}, delimiter=",", autostrip=True, skip_header=1, dtype=float)


plt.subplot(2,1,1) # Der er 2 rækker, 1 kolonne og jeg plotter i 1 række. Skal lære at bruge sharex: sharex=True!
plt.plot(timestamps, ECG, label="ECsG", color="red")
plt.title="ECG"
plt.ylabel("U(uV)")

plt.subplot(2,1,2)
plt.plot(timestamps, PCG, label="PCG")
plt.title="PCG"
plt.ylabel("Enhed")
plt.xlabel("Time(S)")

plt.show()

