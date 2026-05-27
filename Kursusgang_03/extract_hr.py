import matplotlib.pyplot as plt

class HeartRate:
    def __init__(self, file_path:str, Fs:int): # Fs kan være en int. Kan både bruge : og =
        self.gem_data = []
        with open(file_path, "r") as f:
            self.header = f.readline() # Her læses headeren - den bliver dog ikke appended til listen
            for line in f:
                line = line.strip() # Fjerner mellemrum fra start og slut af en linje
                if line:
                    self.gem_data.append(float(line)) # Gemmer dataen i en liste
        self.Ts = [i/Fs for i in range (len(self.gem_data))] # Beregner perioden mellem hver måling 1/Fs = Ts
    
        self.Fs = Fs # Dette gør at den næste metode kan læse Fs
    
    def calculate_heartrate(self, thr:float):
        value_record = 0 # Den optagede værdi
        time_record = 0 # Den optagede tid
        t_old = None # Den gamle tid som slet ikke findes som værdi - dvs. der kan ikke tilføjes nogen værdi hertil?
        heartrate = [] # Pulsen
        timestamps = [] # Tiden målt til pulsslagene
        
        for i, value in enumerate(self.gem_data): # Enumerate gør at værdierne i listen automatisk læses
            if value > thr:
                if value > value_record:
                    value_record = value
                    time_record = i / self.Fs # Dette beregner hvor meget tid der er gået da 1/Fs er 1 periode, så vil fx 5/Fs være 5 perioder, og den tid det tager mellem pulsslag
            else:
                if value_record > 0:
                    if t_old is not None: # Hvis værdien faktisk findes
                        hr = 60 / (time_record - t_old) # Fx 60 s/min / 2 s/slag  = 30 slag/min
                        heartrate.append(hr)
                        timestamps.append(time_record)
                    t_old = time_record # Skal være udenfor if loopet. Husker tiden til det sidste hjerteslag
                value_record = 0 # Resetter variablen i dette loop
                time_record = 0 # Samme her
        return(heartrate, timestamps)

if __name__ == "__main__": # Dette gør åbenbart at programmet ikke åbner ved download - så det skal exekveres først, main skal køres.
    Signal = HeartRate("/home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/oop_3/files/data_1_rows.csv", Fs=300)
    heartrate, timestamps = Signal.calculate_heartrate(thr=0.6)
    plt.subplot(2,1,1) # Deler plots op, så de ikke vises i en graf. Det sidste tal indikerer hvilket plot nummer det er
    plt.plot(timestamps, heartrate) # Når data plottes skal x-aksen plottes først
    plt.title("EKG signal fra en fil") # title og labels bliver kun sat på det subplot de hører til, derfor skal der skrives labels de korrekte steder for formatering
    plt.ylabel("Heartrate (bpm)") 
    
    plt.subplot(2,1,2)
    plt.plot(Signal.Ts, Signal.gem_data)
    plt.xlabel("Tid(s)")
    plt.ylabel("EKG (uV)")
    
    plt.legend()
    plt.show()
    

# /home/Malik/Documents/VS Code/ST/Anvendt programmering/all_lectures/oop_3/files/data_1_rows.csv