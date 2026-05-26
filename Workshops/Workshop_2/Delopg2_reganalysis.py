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
    
    for day in range(len(ppg_sig_lst)): # Ydre matrix/liste er 2 lang
        for ch in range(len(ppg_sig_lst[day])): # Indre matrix/liste er 4 lang
            ppg_sig_lst[day][ch] = DP.bandpass(ppg_sig_lst[day][ch], fs_PPG, lowcut_PPG, highcut_PPG)
    
    ##### Udtræk features #####
    rr_lst = []
    amp_lst = []
    rt_lst = []
    for i in range(len(ECG_signal_lst)):
        r_peaks, r_amplitude, rr_int, thr_ecg = FE._r_peaks(ECG_signal_lst[i], fs_ECG, thr_mult_ECG)
        t_peaks = FE.t_peaks(ECG_signal_lst[i], r_peaks, rr_int)

        t_peaks = np.array(t_peaks)
        match_r_peaks = r_peaks[:len(t_peaks)]
        rt_int = t_peaks - match_r_peaks

        rr_lst.append(rr_int)
        amp_lst.append(r_amplitude["peak_heights"])
        rt_lst.append(rt_int)
    
    ppi_lst = [[], []]
    pulse_width_lst = [[], []]

    for i in range(len(ppg_sig_lst)):
        for j in range(len(ppg_sig_lst[i])):
            ppg_peak, ppg_amplitude, ppi, thr = FE._r_peaks(ppg_sig_lst[i][j], fs_PPG, thr_mult_PPG)
            pulse_width, onset_idx, offset_idx = FE.pulse_width_onoff(time_ppg_lst[i], ppg_sig_lst[i][j])

            ppi_lst[i].append(ppi)
            pulse_width_lst[i].append(pulse_width)
    
    ##### Plot værdierne #####
    feature_label_ecg = ["rr", "amplitude", "rt"]
    data_ecg = [rr_lst, amp_lst, rt_lst]

    for i in range(len(feature_label_ecg)):
        x = np.array(data_ecg[i][0]) # i = hvilken feature der ønskes og 0/1 = dag 1/2
        y = np.array(data_ecg[i][1])

        shortest_list = min(len(x), len(y)) # Kan kun plotte hvis listerne er lige lange
        x = x[:shortest_list]
        y = y[:shortest_list]
        a, b, y_pred, r2 = DA.LinReg(x, y)

        plt.title(f"Day 1 and 2 for {feature_label_ecg[i]}")
        plt.scatter(x, y)
        plt.plot(x, y_pred, label = (f"{a:.2f}x + {b:.2f}, r² = {r2:.2f}"))
        plt.xlabel("Day 1")
        plt.ylabel("Day 2")
        plt.legend()
        filename = f"Workshops/Workshop_2/files_generated/{feature_label_ecg[i]}_list.png"
        DP.save_plot(filename)
        plt.show()

    feature_label_ppg = ["PPI", "Pulse Width"]
    measurement_label_ppg = ["c880", "c660", "b880", "b660"]
    days_label = ["Day 1", "Day 2"]
    data_ppg = [ppi_lst, pulse_width_lst]

    for feat in range(len(feature_label_ppg)):
        for ch in range(len(measurement_label_ppg)):
            x = data_ppg[feat][0][ch] # Bruges til at samle arrays, som ellers kan være svære at plotte
            y = data_ppg[feat][1][ch]

            shortest_list = min(len(x), len(y)) # Kan kun plotte hvis listerne er lige lange
            x = x[:shortest_list]
            y = y[:shortest_list]
            a, b, y_pred, r2 = DA.LinReg(x, y)

            plt.title(f"Day 1 and 2 for {feature_label_ppg[feat]} - {measurement_label_ppg[ch]}")
            plt.scatter(x, y)
            plt.plot(x, y_pred, label = (f"{a:.2f}x + {b:.2f}, r² = {r2:.2f}"))
            plt.xlabel("Day 1")
            plt.ylabel("Day 2")
            plt.legend()
            DP.save_plot(f"Workshops/Workshop_2/files_generated/{feature_label_ppg[feat]}_{measurement_label_ppg[ch]}.png")
            plt.show()

    ##### Gem csv filer #####
    for day in range(2):
        shortest_list = min(len(data_ecg[feat][day]) for feat in range(len(feature_label_ecg))) # Finder de korteste lister
        day_data = [data_ecg[feat][day][:shortest_list] for feat in range(len(feature_label_ecg))] # Slicer data
        filename = f"Workshops/Workshop_2/files_generated/ecg_results_day{day+1}.csv"
        DP.save_csv(filename, feature_label_ecg, np.column_stack(day_data))
            
    for feat in range(len(feature_label_ppg)):
        for day in range(2): 
            shortest_list = min(len(data_ppg[feat][day][ch]) for ch in range(len(measurement_label_ppg))) # Finder de korteste lister
            day_data = [data_ppg[feat][day][ch][:shortest_list] for ch in range(len(measurement_label_ppg))] # Slicer data
            header = [f"{feature_label_ppg[feat]}_{measurement_label_ppg[ch]}" for ch in range(len(measurement_label_ppg))]
            filename = f"Workshops/Workshop_2/files_generated/{feature_label_ppg[feat]}_day{day+1}.csv"
            DP.save_csv(filename, header, np.column_stack(day_data))
            # PPG CSV filen bliver meget kort pga. pulse width er meget kort, og de to features skal være lige lange for at
            # gemme i samme liste. Alternativt kunne de gemmes hver i seperate csv filer, så behøves de ikke matche i længde