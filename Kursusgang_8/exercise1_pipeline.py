import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sp

"""
1. Reproducerbar pipeline - indlæser og visualiserer EKG/PPG
2. Filtrer støj (envelope, rectify, butter, window mean)
3. Uddrage relevante features
4. Gem data i en CSV fil

Visualiser data -> filtrer data -> udtræk features 

Regressionsanalyse

Refractrurering -> (Omdanner koden - så den bliver mere overskueligt, laver classes/funktioner)

Navngivning og cash invalidation er svært

Lav det så det virker --> lav det om til OOP --> regressions analyse (fortolk disse og hvad det betyder)

Features ud af signaler:
RR
RT
R amplitude
Pulse widht

PPI (pulse interval)

ECG: 500 Hz
PPG: 100 Hz
"""
def moving_average(values,windowsize):
    kernel = np.ones(windowsize)/windowsize
    filtered_signal = np.convolve(values, kernel, mode = "same")
    return filtered_signal

ECG_file = "/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_4_workshop/files/10_18-12-33_ecg.csv"
PPG_file = "/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_4_workshop/files/10_18-12-33_ppg.csv"

ECG_timestamps, ECG_leadv1, ECG_leadv2, ECG_leadv3, ECG_leadv4 = np.genfromtxt(ECG_file, unpack=True, delimiter=",", autostrip=True, skip_header=1)
PPG_timestamps, PPG_carotid880nm, PPG_carotid660nm, PPG_brachiel880nm, PPG_brachiel660nm = np.genfromtxt(PPG_file, unpack=True, delimiter=",", autostrip=True, skip_header=1)

# Slicer signalet, fordi de første og sidste signaler virker underlige - måske bandpasse den istedet
sliceSignal = slice(200, 1000)
ECG_timestamps = ECG_timestamps[sliceSignal]
ECG_leadv1 = ECG_leadv1[sliceSignal]
ECG_leadv2 = ECG_leadv2[sliceSignal]
ECG_leadv3 = ECG_leadv3[sliceSignal]
ECG_leadv4 = ECG_leadv4[sliceSignal]

rawSignal = ECG_leadv1

# Filtrer signalet ift. frekvenser 
fs_ECG = 1/0.002 # Omregning til herz
b, a = sp.butter(2, [1, 30], fs=fs_ECG, btype="bandpass") # Skal highpass, fordi EKG ligge rmellem 10-15 Hz
ButterRaw = sp.filtfilt(b,a, ECG_leadv1)
ECG_leadv1 = sp.filtfilt(b,a,ECG_leadv1)
ECG_leadv2 = sp.filtfilt(b,a,ECG_leadv2)
ECG_leadv3 = sp.filtfilt(b,a,ECG_leadv3)
ECG_leadv4 = sp.filtfilt(b,a,ECG_leadv4)

# Filtrer støj vha. moving average
window_size = 10
ECG_leadv1 = moving_average(ECG_leadv1, window_size)
ECG_leadv2 = moving_average(ECG_leadv2, window_size)
ECG_leadv3 = moving_average(ECG_leadv3, window_size)
ECG_leadv4 = moving_average(ECG_leadv4, window_size)

# Omdanner dem til numpy arrays - så de kan lægges sammenordentligt
array_leadv1 = np.array(ECG_leadv1)
array_leadv2 = np.array(ECG_leadv2)
array_leadv3 = np.array(ECG_leadv3)
array_leadv4 = np.array(ECG_leadv4)
#leadSum = array_leadv1 + array_leadv2 + array_leadv3 + array_leadv4

# Enveloper (tæpper) 
env_ECG1 = sp.envelope(ECG_leadv1)[0] # Første liste
env_ECG2 = sp.envelope(ECG_leadv2)[0]
env_ECG3 = sp.envelope(ECG_leadv3)[0]
env_ECG4 = sp.envelope(ECG_leadv4)[0]
#env_ECG = sp.envelope(leadSum)[0]

r_peaks1, r_amplitude1 = sp.find_peaks(env_ECG1, height=np.std(env_ECG1), distance=int(0.1*fs_ECG)) 
r_peaks2, r_amplitude2 = sp.find_peaks(env_ECG2, height=np.std(env_ECG2), distance=int(0.1*fs_ECG)) 
r_peaks3, r_amplitude3 = sp.find_peaks(env_ECG3, height=np.std(env_ECG3), distance=int(0.1*fs_ECG)) 
r_peaks4, r_amplitude4 = sp.find_peaks(env_ECG4, height=np.std(env_ECG4), distance=int(0.1*fs_ECG)) 

#r_amplitude1 = r_amplitude1["peak heights"]

print(r_amplitude1)
RR1 = np.diff(r_peaks1)
RR2 = np.diff(r_peaks2)
RR3 = np.diff(r_peaks3)
RR4 = np.diff(r_peaks4)

RR1_mean = np.mean(RR1)
RR2_mean = np.mean(RR2)
RR3_mean = np.mean(RR3)
RR4_mean = np.mean(RR4)

# Finder t peaks!

# Finder t-peaks skal lave windows


# The fuck this shit do?
plt.plot(ECG_timestamps, ECG_leadv1, label="Lead v1")
plt.plot(ECG_timestamps, ButterRaw, label="ButterRaw", color="pink")
plt.plot(ECG_timestamps, env_ECG1, color = "orange")
plt.scatter(ECG_timestamps[r_peaks1], env_ECG1[r_peaks1], color = "red", label = f"R peaks (RR = {int(RR1_mean)} ms)")
#plt.scatter(ECG_timestamps[t_peaks1], env_ECG1[t_peaks1], color = "black")


"""
t_peaks1 = [] # Laver tom liste
t_peaks2 = [] # Laver tom liste
t_peaks3 = [] # Laver tom liste
t_peaks4 = [] # Laver tom liste
t_window = (RR1*0.1).astype(int) # Gemmer et lille vindue som integer
t_window = (RR2*0.1).astype(int) # Gemmer et lille vindue som integer
t_window = (RR3*0.1).astype(int) # Gemmer et lille vindue som integer
t_window = (RR4*0.1).astype(int) # Gemmer et lille vindue som integer
envLeadSum = env_ECG1+env_ECG2+env_ECG3+env_ECG4
plt.plot(ECG_timestamps, ECG_leadv2, label="Lead v2")
plt.plot(ECG_timestamps, ECG_leadv3, label="Lead v3")
plt.plot(ECG_timestamps, ECG_leadv4, label ="Lead v4")
plt.plot(ECG_timestamps, leadSum, label="Lead sum")
plt.plot(ECG_timestamps, env_ECG, label ="Envelope")
plt.plot(ECG_timestamps, envLeadSum, label ="Envelope lead sum")

I find peaks - skru op for distance - for at ignorere støj (dobbelt r takker, som muligvis blot er kontrahering af hjertet)
Derudover overvej histogrammer, for at finde forhold af RR peaks o.l.

Det er også muligt at plt.xlim i stedet for at slice
for i in range(len(RR1)): # Burde kunne dobbel loope this one
    start = r_peaks1[i]+ t_window[i]
    end = r_peaks1[i+1] - t_window[i]
    if end > start:
        RR_window = env_ECG1[start:end] # Kan kun tage integers, ingen floats
        RR_window_idx = np.argmax(RR_window) # The fuck this shit do?
        t_peaks1.append(start + RR_window_idx)

plt.legend()
plt.show()
"""

