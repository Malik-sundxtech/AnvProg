import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sp

def moving_average(self, thr, window=50):
    if PCG > thr:
        start = PCG
    
file = "/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_2/files/ECGPCG.csv"

timestamps, ECG, PCG = np.genfromtxt(file, unpack=True, usecols={0,1,2}, autostrip=True, delimiter=",",skip_header=1, dtype=float)


fs=1/0.000125 # I filen ses en periode på 0.000125 s, 1/Ts = Fs (8000)
b, a = sp.butter(2, [1,150], fs=fs, btype="bandpass") 

""" Butter: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
butter(N, Wn, btype='low', analog=False, output='ba', fs=None
    Butter filtrer specifikke frekvenser fra.
    Giver et b og a IIR(infinite impulse response) filter
    Bruges til at smoothe ting ud - buttering out
    
N: Filtre ordenen. Højere tal jo højere orden filtrering og ofte bedre frasortering af støj
Wn: Et array for de kritiske frekvenser til lowpass og highpass filtre
btype(bandtype): Definerer lowpass, highpass, bandpass, no pass
fs: Samplings frekvens
"""

ECG = sp.filtfilt(b, a, ECG)

""" Filtfilt: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html
filtfilt(b, a, x, axis=-1, padtype='odd', padlen=None, method='pad', irlen=None)
    Tilføjer et digitalt filter forud og bagud for signalet
    Anvender IIR (dobbelt filtrering) - gør at de "bump" der ønskes forbliver

a og b danner en brøk
b: Tæller koefficient
a: Nævner koefficient
x: Det array der skal filtreres - fx et ECG signal
"""


env_ECG = sp.envelope(ECG)[0]
""" Envelope: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.envelope.html
envelope(z, bp_in=(1, None), *, n_out=None, squared=False, residual='lowpass', axis=-1)


"""

r_peaks, _ = sp.find_peaks(env_ECG, height=np.std(env_ECG), distance=int(0.3*fs)) 
""" Find peaks: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
find_peaks(x, height=None, threshold=None, distance=None, prominence=None, width=None, wlen=None, rel_height=0.5, plateau_size=None)
    Returneres som indices/tuples. _ gør at nogen værdier igoreres (throwaway variable) dvs. extra info såsom 
    Der findes 2 lister i r_peaks, _ fortæller at jeg kun vil have den ene liste
x: Det signal der ønskes at finde toppunkter til
height: Hvis der kræves en højde af amplituden
distance: Minimum afstand på x-aksen - for det meste i tiden
threshold: distance threshhold

"""


# Finder t-peaks skal lave windows

RR_time = np.diff(r_peaks) # Finder ud af hvor mange sekunder der er mellem peaks
t_peaks = [] # Laver tom liste
t_window = (RR_time*0.1).astype(int) # Gemmer et lille vindue som integer


for i in range(len(RR_time)):
    start = r_peaks[i]+ t_window[i]
    end = r_peaks[i+1] - t_window[i]
    if end > start:
        RR_window = env_ECG[start:end] # Kan kun tage integers, ingen floats
        RR_window_idx = np.argmax(RR_window) # The fuck this shit do?
        t_peaks.append(start + RR_window_idx)
        

plt.plot(timestamps, ECG, label="Raw")
plt.plot(timestamps, env_ECG, alpha=0.9, label="Envelope")
plt.scatter(timestamps[r_peaks], env_ECG[r_peaks], color="red", label = "R peaks") # Punktplot
plt.scatter(timestamps[t_peaks], env_ECG[t_peaks], color = "crimson", label = "T peaks")
plt.title("Raw, env, R- og T-peaks")

plt.xlabel("Time(s)")
plt.legend()
plt.show()
