import matplotlib.pyplot as plt
import numpy as np

def moving_average(x, winsize = 50): #Funktion til at tage lokalt gns af signalet x
    filtered_x = np.zeros_like(x)
    
    for i in range(len(x)):
        start = i - winsize//2 # // giver heltal, da det er integers. Det har noget med offsetting af data at gøre, så det ikke bliver forskudt i tid
        stop = i + winsize//2
        
        if start < 0: # Sikrer at winsize ikke tage en værdi under 0
            start = 0
        if stop > len(x): # Sikrer at winsize ikke tager en værdi over max
            stop = len(x)    
        slice = x[start:stop]
        filtered_x[i] = slice.mean()
    return filtered_x

def moving_average_offset(x, winsize = 50): #Funktion til at tage lokalt gns af signalet x
    filtered_x = np.zeros_like(x)
    
    for i in range(len(x)):
        start = i - winsize # Hvis winsize ændres til 25, gør denne funktion præcis det samme og der er ikke behov for at dividere med 2
        stop = i + winsize
        
        if start < 0: # Sikrer at winsize ikke tage en værdi under 0
            start = 0
        if stop > len(x): # Sikrer at winsize ikke tager en værdi over max
            stop = len(x)    
        slice = x[start:stop]
        filtered_x[i] = slice.mean()
    return filtered_x

signal1 = np.genfromtxt("/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_1/files/random_signal1.csv")
signal2 = np.genfromtxt("/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/signals_1/files/random_signal2.csv")

Ts = 1 / len(signal1) # Tidsperioden beregnes
Fs = 1 / Ts # Frekvensen beregnes
T = np.linspace(0, 1000, len(signal1)) # Den skal laves for at få linjer plottet ind. Dvs. mean og std. Plads 2 skalrer aksen

signal1_mean = np.mean(signal1)
signal1_std = np.std(signal1)
signal1_filtered = moving_average(signal1)
signal_filtered_offset = moving_average_offset(signal1)



plt.plot(T, signal1, label="Rå signal", alpha=0.5) # Billedet bliver lavet men ikke vist. Men det er effektivt hvis de skal laves uden at vise dem
#plt.plot(signal2)



plt.plot( # Plotter de positive værdier
    [0, 1000], # Dette betyder plot fra x_0 til x_1 e.g. 0-1000 på x-aksen
    [signal1_mean + signal1_std, signal1_mean + signal1_std], # Skal skrive hvad den skal plotte 2 gange, fordi det er fra start og til slut af signalet den skal plotte dem
    linestyle="--",
    color="red",
    label="Gennemsnit+afvigelse",
)
plt.plot( # plotter de negative værdier
    [0, 1000],
    [signal1_mean - signal1_std, signal1_mean - signal1_std],
    linestyle="--",
    color="black",
    label="Gennemsnit-afvigelse",
)
plt.plot(signal1_filtered, color="black", label="Filtreret signal")
plt.plot(signal_filtered_offset, color="red", label="Filtreret signal offset")

plt.title("Signaler visualiseres")
plt.xlabel("Time (s)")
plt.ylabel("Ampltiude")
plt.legend() # Viser labels for hvert enkelt element
plt.show()