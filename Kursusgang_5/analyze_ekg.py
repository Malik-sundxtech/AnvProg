import matplotlib.pyplot as plt
import numpy as np
import math as math

def peak_detector(data:list[float], thr:float):
    value_record = 0
    time_record = 0
    indencies: list[float] = []
    
    for i, value in enumerate(data):
        if value > thr: # Fjerner støj vha. threshhold, ellers ville den få random toppunkter, når der sker en tilfældig målefejl, da det næste punkt ikke er større
            if value > value_record:
                value_record = value
                time_record = i
        else:
            if value_record:
                indencies.append(time_record)
                value_record = 0
                time_record = 0
    return indencies


file = "ST/Anvendt programmering/all_lectures/signals_1/files/ECG_300Hz.csv"
index, ecg = np.genfromtxt(file, unpack=True, skip_header=1, delimiter=",", usecols={0, 1}, autostrip=True, dtype=float)
tid = index / 300 # Fs = 300, derfor tager det 1 s at lave 300 målinger og derfor er 300 /målinger / 300 målinger/s = 1 s


ecg_mean = np.mean(ecg)
ecg_std = np.std(ecg)

peaks = peak_detector(ecg, 0.6)
time_diff_peaks = np.diff(peaks) / 300 # Dividerer med 300 for at konvertere til sekunder her.

ecg_SDNN = np.std(time_diff_peaks, ddof=1) # Udtrykker HRV. Std af tid mellem peaks (R til R). ddof(delta degrees of freedom, i = 1, hvor stor inkrementioner der sker af x i formlen for std)
print(f"SDNN er {ecg_SDNN}")

ecg_RMSDD = np.sqrt(np.mean(np.diff(time_diff_peaks)**2)) # ** anden potens. diff(time...) her beskriver tidsvariationen mellem slag
print(f"RMSDD er {ecg_RMSDD}")


metrics = [ecg_mean,ecg_std, ecg_SDNN, ecg_RMSDD]
labels = ["Mean", "Std", "SDNN", "RMSDD"]

plt.figure(figsize=(5,4))
plt.bar(labels, metrics, color=["green", "pink", "red", "blue"])
plt.ylabel("Time (s)") # = assigner, () kalder funktion
plt.title("HRV metrics")
plt.ylim(0, max(metrics)*1.1) # Sætter grænser for y-aksen, max er den største værdi i datasættet
plt.tight_layout() # Akserne kan nogen gange forsvinder, pga. plads mangel, denne funktion forhindrer dette
plt.show()



""" Gammel kode
plt.plot(tid, ecg, label="EKG")
plt.xlabel = "Tid (s)"
plt.ylabel = "EKG (uV)"
plt.title = "EKG over tid"
plt.plot(
    [0, 2],
    [ecg_mean+ecg_std, ecg_mean+ecg_std],
    linestyle ="--",
    color="red",
    label ="Gns+std afvig"
)
plt.plot(
    [0, 2],
    [ecg_mean-ecg_std, ecg_mean-ecg_std],
    linestyle="--",
    color="red",
    label="Gns-std afvig"
)

plt.figure(figsize=[4,5]) # Hvor bred figuren skal skaleres i x- og y-aksen
plt.boxplot(ecg)
plt.errorbar(1.1, ecg_mean, yerr=ecg_std, fmt="o", color="red", markersize=5, capsize=5, label="Mean ±1 std") # Markersize og ikke marksize
plt.xticks=([1], ["ecg"]) # Giver datanummer 1 navnet ecg

plt.legend()
plt.show()
"""
""" Forklaringer
Mean
Std - standard deviation
Sdnn - Standard deviation of NN intervals. Matematisk set normal std, men fra peak til peak (R til R i hjerteslag)
    Udtrykker HRV. Std af tid mellem peaks (R til R).
RMSSD - Root mean square of successive differences

SDNN og RMSSD er begge to måder at regne HRV(heartrate variability) på, men udtrykker lidt forskellige ting. SDNN er mere til langtidsovervågning e.g. 24 timer
SDNN fortæller noget om ANS aktivitet
RMSSD er kort tid, fra slag til slag, og fortæller noget om parasympatisk aktivitet
SDNN mere brugt i klinisk sammenhæng og fortæller noget om para- og sympatisk aktivitet
RMSSD mere ift. sportsrestitution - primært parasympatisk aktivitet

genfromtxt info:
    unpack = true (hvis dataen skal gemmes i flere lister e.g. x, y = ...)
    skipheader = 1 (skipper 1 linje, kan ændres)
    delimiter = "," (stripper alle kommaer væk, seperer dataerne)
    usecol = {0,1} (hvilken kolonne der skal bruges i dette tilfælde nr 0 og 1)
    autostrip = true (Fjerner alle mellemrum)
    dtype = (datatype)

plt.errorbar:
    plt.errorbar(1.1, ecg_mean, yerr=ecg_std, fmt="o", color="red", markersize=5, capsize=5, label="Hej")
    1.1 er hvor den befinder sig på x-aksen, hvis denne værdi =1 betyder det at errorbaren er ovenpå boxplottet
    markersize (størrelsen på prikken - gns)
    yerr (y-error, det er bare en vilkårlig variabel navn)
    fmt(format)="o" - lav en cirkel, "x" for kryds
    capsize er længden endepunkternes ben
"""