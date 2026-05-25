##### Hardcodede values #####
fs_ECG = 500
highcut_ECG = 150
lowcut_ECG = 10
thr_mult_ECG = 2

fs_PPG = 100
highcut_PPG = 25
lowcut_PPG = 1
thr_mult_PPG = 0.3
##### Hardcodede values #####


# Importer relevante biblioteker
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sps
from sklearn.linear_model import LinearRegression
from Delopg1_signalanalysis import DataProcessing
from Delopg1_signalanalysis import FeatureExtractor

# Laver en metode til reg
class DataAnalysis():
    def LinReg(self, x, y):
        x = np.array(x).reshape(-1, 1)
        y = np.array(y)

        LR = LinearRegression()
        LR.fit(x, y)

        slope = LR.coef_[0]
        intercept = LR.intercept_
        y_pred = LR.predict(x)
        r2 = LR.score(x, y)

        return slope, intercept, y_pred, r2


DP = DataProcessing()
FE = FeatureExtractor()
DA = DataAnalysis()

if __name__ == "__main__":
    #################### Extraher og sæt værdier i lister ####################
    filepath_ecg = ["Workshops/Workshop_2/files/10_18-12-33_ecg.csv", "Workshops/Workshop_2/files/10_18-13-23_ecg.csv"]
    time_ecg_lst = []
    ECG_signal_lst = []

    for i in range(len(filepath_ecg)):
        time_ecg, v1, v2, v3, v4 = DP.extract_file(filepath_ecg[i])
        ecg_leads = [v1, v2, v3, v4]
        ECG_signal = sum(ecg_leads)
        
        time_ecg_lst.append(time_ecg)
        ECG_signal_lst.append(ECG_signal)
    

    filepath_ppg = ["Workshops/Workshop_2/files/10_18-12-33_ppg.csv", "Workshops/Workshop_2/files/10_18-13-23_ppg.csv"]
    time_ppg_lst = []
    ppg_sig_lst = []
    
    for i in range(len(filepath_ppg)):
        time_ppg, c880, c660, b880, b660 = DP.extract_file(filepath_ppg[i])
        ppg_sig = [c880, c660, b880, b660]

        time_ppg_lst.append(time_ppg)
        ppg_sig_lst.append(ppg_sig) # Laver en 2x4 datamatrix (2 lister med 4 lister/datasæt i)
    
    ##### Filtrer støj fra alle signaler (ECG og PPG) #####
    for i in range(len(ECG_signal_lst)):
        ECG_signal_lst[i] = DP.bandpass(ECG_signal_lst[i], fs_ECG, lowcut_ECG, highcut_ECG)
    
    for i in range(len(ppg_sig_lst)): # Ydre matrix/liste er 2 lang
        for j in range(len(ppg_sig_lst[i])): # Indre matrix/liste er 4 lang
            ppg_sig_lst[i][j] = DP.bandpass(ppg_sig_lst[i][j], fs_PPG, lowcut_PPG, highcut_PPG)
    
    ##### Udtræk features #####
    rr_mean_lst = []
    amp_mean_lst = []
    rt_mean_lst = []
    for i in range(len(ECG_signal_lst)):
        r_peaks, r_amplitude, rr_int, thr_ecg = FE.r_peaks(ECG_signal_lst[i], fs_ECG, thr_mult_ECG)
        t_peaks = FE.t_peaks(ECG_signal_lst[i], r_peaks, rr_int)

        rr_mean = np.mean(rr_int)
        amp_mean = np.mean(r_amplitude["peak_heights"])

        t_peaks = np.array(t_peaks)
        match_r_peaks = r_peaks[:len(t_peaks)]
        rt_int = t_peaks - match_r_peaks
        rt_mean = np.mean(rt_int)

        rr_mean_lst.append(rr_mean)
        amp_mean_lst.append(amp_mean)
        rt_mean_lst.append(rt_mean)
    
    ppi_lst = [[], []]
    pulse_width_lst = [[], []]

    for i in range(len(ppg_sig_lst)):
        for j in range(len(ppg_sig_lst[i])):
            ppg_peak, ppg_amplitude, ppi, thr = FE.r_peaks(ppg_sig_lst[i][j], fs_PPG, thr_mult_PPG)
            pulse_width, onset_idx, offset_idx = FE.pulse_width_onoff(time_ppg_lst[i], ppg_sig_lst[i][j])

            ppi_lst[i].append(ppi)
            pulse_width_lst[i].append(pulse_width)
    
    ##### Plot værdierne #####
    feature_label_ecg = ["rr", "amplitude", "rt"]
    data_ecg = [rr_mean_lst, amp_mean_lst, rt_mean_lst]

    for i in range(len(feature_label_ecg)):
        x = np.concatenate(data_ecg[0][i])
        y = np.concatenate(data_ecg[1][i])

        shortest_list = min(len(x), len(y)) # Kan kun plotte hvis listerne er lige lange
        x = x[:shortest_list]
        y = y[:shortest_list]
        a, b, y_pred, r2 = DA.LinReg(x, y)

        plt.title(f"Day 1 and 2 for {feature_label_ecg[i]}")
        plt.scatter(x, y)
        plt.plot(x, y_pred, label = (f"{a:.2f}x + {b:.2f}, Determinations koefficient = {r2:.2f}"))
        plt.xlabel("Day 1")
        plt.ylabel("Day 2")
        plt.legend()
        plt.show()

    feature_label_ppg = ["PPI", "Pulse Width"]
    days_label = ["Day 1", "Day 2"]
    data_ppg = [ppi_lst, pulse_width_lst]

    for i in range(len(feature_label_ppg)):
        x = np.concatenate(data_ppg[0][i]) # Bruges til at samle arrays, som ellers kan være svære at plotte
        y = np.concatenate(data_ppg[1][i])
        # i = featuren (PPI eller Pulse width)
        shortest_list = min(len(x), len(y)) # Kan kun plotte hvis listerne er lige lange
        x = x[:shortest_list]
        y = y[:shortest_list]
        a, b, y_pred, r2 = DA.LinReg(x, y)

        plt.title(f"Day 1 and 2 for {feature_label_ppg[i]}")
        plt.scatter(x, y)
        plt.plot(x, y_pred, label = (f"{a:.2f}x + {b:.2f}, Determinations koefficient = {r2:.2f}"))
        plt.xlabel("Day 1")
        plt.ylabel("Day 2")
        plt.legend()
        plt.show()