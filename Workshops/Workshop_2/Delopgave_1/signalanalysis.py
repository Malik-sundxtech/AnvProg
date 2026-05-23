""" Ordforklaring
v = vektor (den vektor et lead danner) 
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sps
time, v1, v2, v3, v4 = np.genfromtxt("Workshops/Workshop_2/Delopgave_1/files/10_18-12-33_ecg.csv", 
                                     unpack=True,
                                     delimiter=",",
                                     autostrip=True, 
                                     skip_header=1)

class DataCleaner():
    def bandpass(self, data, fs=2000, lowcut=10, highcut=250, order=4): 
        '''###-bandpass-filter-###'''
        low = lowcut / (fs/2) #normaliseret cutoff-frekvens(mellem 0 og 1)
        high = highcut / (fs/2) #normaliseret cutoff-frekvens(mellem 0 og 1)
        b, a = sps.butter(order, [low, high], btype='band') 

        '''###-zero-phase-filter-###'''
        filtered_bandpass_signal = sps.filtfilt(b, a, data)#This function applies a linear digital filter twice, once forward and once backwards. The combined filter has zero phase, hvilket betyder at når der filtreres begge veje undgås forskydning af x-aksen
        return filtered_bandpass_signal



DC = DataCleaner()

ECG_signal = v1+v2+v3+v4

ECG_signal = DC.bandpass(ECG_signal)
plt.plot(time, ECG_signal)
plt.show()