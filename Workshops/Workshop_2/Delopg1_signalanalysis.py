""" Ordforklaring og opgavebeskrivelse
##### Ordforklaring #####
ECG:
    leads = v1, v2, v3 og v4
    v = vektor (den vektor et lead danner)

PPG:
   brachiel (armen)
   carotid (nakken)
   660 nm - rødt lys
   880 nm - infrarødt lys

##### Opgavebeskrivelse #####
ECG
    Beregn RR og RT interval samt R amplitude for ECG
PPG
    Beregn PPI (pulse to puls interval) and pulse width for PPG

Forkortelser:
    idx = index
    l, lst = list
    fs = frequency
    mult = multiplier
    thr = threshold
    d, dist, dst = distance
    amp = amplitude
    p, pk = peak
    sig = signal
    inv = inverted


##### Besvarelse af spørgsmål ######
Fortolkning af resultater:
Etiske overvejelser: databeskyttelse, anonymitet og dataminimering

Skal yderligere implementeres: 
    beskyttet data
    Her lige fundet ud af der findes en peak_widths funktion:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.peak_widths.html#scipy.signal.peak_widths
"""


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

# Definer relevante klasser og metoder
class DataProcessing():
    def extract_file(self, filepath):
        return np.genfromtxt(filepath, 
                             unpack=True,
                             delimiter=",",
                             autostrip=True, 
                             skip_header=1)
    def save_csv(self, filepath, headers, data): # Gemmer data i en csv fil
        np.savetxt(filepath, data, delimiter=",", header=",".join(headers), comments="")

    def save_plot(self, filepath):
        plt.savefig(filepath)

    def bandpass(self, data, fs, lowcut, highcut, order=4): # Evt. yderligere forklaring
        low = lowcut / (fs/2) 
        high = highcut / (fs/2) 
        b, a = sps.butter(order, [low, high], btype='band') 
        filtered_bandpass_signal = sps.filtfilt(b, a, data) 
        return filtered_bandpass_signal
    
class FeatureExtractor():
    def r_peaks(self, signal, fs, thr_multiplier, time_interval = 0.5):
        thr = np.mean(signal) + thr_multiplier*np.std(signal) 
        dst = fs*time_interval

        r_peaks, r_ampltidues = sps.find_peaks(signal, distance = dst, height = thr)
        # Height er threshold (y-aksen)
        # Distance er hvor lang tid (x-aksen) der skal gå for der kan findes et nyt toppunkt
        interval = np.diff(r_peaks)
        return r_peaks, r_ampltidues, interval, thr
    
    def t_peaks(self, signal, r_peaks, rr_int):
        t_peaks = []
        for i in range(len(rr_int)): # Burde kunne dobbel loope this one
            start = r_peaks[i] + int(0.05 * rr_int[i])
            end = r_peaks[i+1] - int(0.5 * rr_int[i])
            if end > start:
                RR_window = signal[start:end] # Kan kun tage integers, ingen floats
                RR_window_idx = np.argmax(RR_window) # The fuck this shit do?
                t_peaks.append(start + RR_window_idx)
        return t_peaks
    
    def pulse_width_onoff(self, time, sig): 
        pulse_width_list = []
        onset_idx_list = []
        offset_idx_list = []

        # Bestemmer en thr
        sig_mean = np.mean(sig)
        sig_std = np.std(sig)
        thr = sig_mean + 0.001*sig_std 
        above_thr = False 
        for i, value in enumerate(sig):
            if value > thr and not above_thr: # Når værdi er større end thr og når above_thr er False (sikre at der ikke sættes flere onsets)
                onset_index = i
                above_thr = True
            
            elif value < thr and above_thr: # Når værdi er mindre end thr og når above_thr er True
                offset_index = i
                above_thr = False

                # Beregner onset og offset tid
                onset = time[onset_index]
                offset = time[offset_index]
                onset_idx_list.append(onset_index)
                offset_idx_list.append(offset_index)

                # Beregner pulse width
                pulse_width = offset - onset
                pulse_width_list.append(pulse_width)

        return pulse_width_list, onset_idx_list, offset_idx_list

    def pulse_width_min(self, signal, time, fs, thr_multiplier, time_interval=0.3): # Et forsøg, benyt den første metode
        inverted = -signal # Tager den inverse af signalet, så vi kan finde toppunkter for at finde de reelle minimumspunkter
        thr = np.mean(inverted) + thr_multiplier*np.std(inverted)
        dst = fs*time_interval

        ppg_min_idx, _ = sps.find_peaks(inverted, height=thr, distance=dst) 
        pulse_width_list = np.diff(time[ppg_min_idx])

        return pulse_width_list, ppg_min_idx
    
    def pulse_width_find_widths(self):
        pass


# Kører scriptet herinde
if __name__ == "__main__":
    DP = DataProcessing() 
    FE = FeatureExtractor()

    #################### Extraher og sæt værdier i lister ####################
    time_ecg, v1, v2, v3, v4 = DP.extract_file("Workshops/Workshop_2/files/10_18-12-33_ecg.csv")
    time_ppg, c880, c660, b880, b660 = DP.extract_file("Workshops/Workshop_2/files/10_18-12-33_ppg.csv")

    ecg_leads = [v1,v2,v3,v4]
    ECG_signal = sum(ecg_leads)

    ppg_sig = [c880, c660, b880, b660]

    #################### ECG ####################
    # Filtrer støj fra signalet
    ECG_signal = DP.bandpass(ECG_signal, fs_ECG, lowcut_ECG, highcut_ECG)

    # Udtrækker features
    r_peaks, r_amplitude, rr_int, thr_ecg = FE.r_peaks(ECG_signal, fs_ECG, thr_mult_ECG)
    t_peaks = FE.t_peaks(ECG_signal, r_peaks, rr_int)

    # Finder en gennemsnittelig værdi af features
    rr_mean = np.mean(rr_int)
    amp_mean = np.mean(r_amplitude["peak_heights"]) # En af de mange datatyper der gemmes i denne funktion

    # rt interval og gns
    t_peaks = np.array(t_peaks)
    match_r_peaks = r_peaks[:len(t_peaks)]
    rt_int =  t_peaks - match_r_peaks
    rt_mean = np.mean(rt_int)

    # Printer værdierne
    print(f"Average rr interval is: {rr_mean:.2f} and amplitude is {amp_mean:.2f}")
    print(f"Average rt interval {rt_mean:.2f}")
    print("\n")

    # Plot ecg signal
    plt.figure(figsize=(10,10))
    plt.plot(time_ecg, ECG_signal)
    plt.axhline(thr_ecg, linestyle="--", color="black", label="r peak thr")
    plt.scatter(time_ecg[r_peaks], ECG_signal[r_peaks])
    plt.scatter(time_ecg[t_peaks], ECG_signal[t_peaks], color="red")

    plt.legend(loc="upper right")
    DP.save_plot("Workshops/Workshop_2/files_generated/ecg_plot") # Gemmer plottet som fil
    plt.show()

    #################### PPG ####################
    # Filter støj fra alle ppg signaler
    for i in range(len(ppg_sig)):
        ppg_sig[i] = DP.bandpass(ppg_sig[i], fs_PPG, lowcut_PPG, highcut_PPG)

    # Finder features(PPI og pulse width) for alle ppg signaler
    ppg_peaks = []
    ppg_amplitudes = []
    ppi_list = []
    thr_ppg = []

    pulse_width_list = []
    onset_idx_list = []
    offset_idx_list = []

    for i in range(len(ppg_sig)):
        ppg_peak, ppg_amplitude, ppi, thr = FE.r_peaks(ppg_sig[i], fs_PPG, thr_mult_PPG)
        ppg_peaks.append(ppg_peak)
        ppg_amplitudes.append(ppg_amplitude)
        ppi_list.append(np.mean(ppi))
        thr_ppg.append(thr)


    for i in range(len(ppg_sig)):
        pulse_width, onset_idx, offset_idx = FE.pulse_width_onoff(time_ppg, ppg_sig[i])
        pulse_width_list.append(np.mean(pulse_width))
        onset_idx_list.append(onset_idx)
        offset_idx_list.append(offset_idx)


    # Printer værdier
    measurement_labels = ["c880", "c660", "b880", "b660"]
    for i in range(len(ppg_sig)):
        print(f"PPI for {measurement_labels[i]} is {ppi_list[i]:.2f}")
        print(f"Pulse-width for {measurement_labels[i]} is {pulse_width_list[i]:.2f}")
    

    # Plotter PPG signaler
    colors = ["blue", "green", "orange", "red"]
    labels = ["thr_c880", "thr_c660", "thr_b880", "thr_b660"]
    for i in range(len(ppg_sig)):
        # Plot grafen
        plt.plot(time_ppg, ppg_sig[i], color = colors[i])
        
        # Plot peaks og thr
        plt.scatter(time_ppg[ppg_peaks[i]], ppg_sig[i][ppg_peaks[i]], color = colors[i])
        plt.axhline(thr_ppg[i], linestyle="--", color=colors[i], label=labels[i], alpha=0.7)
        
        # Plot onset og offset
        plt.scatter(time_ppg[onset_idx_list[i]], ppg_sig[i][onset_idx_list[i]], color = colors[i], marker = "x")
        plt.scatter(time_ppg[offset_idx_list[i]], ppg_sig[i][offset_idx_list[i]], color = colors[i], marker = "x")

    plt.legend(loc="upper right")
    DP.save_plot("Workshops/Workshop_2/files_generated/ppg_plot") # Gemmer plottet som fil
    plt.show()


    #################### Gem alt data i csv filer ####################
    # ECG
    headers_ecg = ["Ramplitude", "RRinterval", "RTinterval"]
    data_ecg = np.array([[amp_mean, rr_mean, rt_mean]]) # Så data gemmes i kolonner frem for rækker

    DP.save_csv("Workshops/Workshop_2/files_generated/ecg_results.csv", headers_ecg, data_ecg)
    

    # PPG
    headers_ppg = ["PPI", "PulseWidth"]
    data_ppg = np.array([ppi_list, pulse_width_list]).T # Dette er lister så de gemmes anderledes. T = transpose

    DP.save_csv("Workshops/Workshop_2/files_generated/ppg_results.csv", headers_ppg, data_ppg)
    


