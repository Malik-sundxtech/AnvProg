import random 
from datetime import datetime 
import matplotlib.pyplot as plt
import csv

class Measurement:
    def __init__(self, timestamp, value, meas_id):
        self.timestamp = timestamp
        self.value = value
        self.meas_id = meas_id

class Device(): # Template til devices
    def __init__(self, name, device_id, min_val, max_val):
        self.name = name
        self.device_id = device_id 
        self.min_val = min_val
        self.max_val = max_val
        self.measurements = []
        self._counter = 0 # Gør at device id kan tælle op

    def generate_measurement(self):
        self._counter += 1
        value = round(random.uniform(self.min_val, self.max_val), 2) # Generer data. Round 2 = 2 decimaler
        dev_id = f"{self.device_id}_{self._counter:03d}" # Generer device id
        timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")

        measurement = Measurement(timestamp, value=value, meas_id = dev_id) # Gemmer alle data i en samlet liste
        self.measurements.append(measurement) 

class DataCollector(): # Saml data i en CSV fil
    def __init__(self):
        self.devices = [] # Dette er en liste, og skal derfor ikke stå ovenover

    def add_device(self, device):
        self.devices.append(device)

    def collect_all(self, n_measurements):
        for device in self.devices:
            for _ in range(n_measurements):
                device.generate_measurement()

class FileSaving():
    def save_csv(self, filepath, data): # Gemmer data i en csv fil
       with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["device_type", "device_id", "timestamp", "value"]) # Laver headeren
        writer.writerows(data) # Gemmer dataerne 

    def load_csv(self, filepath, device):
        loaded_data = []
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                loaded_data.append(row)
        print(device.name)
        print(f"Forventet 200 rækker, loaded {len(loaded_data)} rækker")

        for row in loaded_data:
            value = float(row["value"])
            if row["device_type"] == device.name:
                assert device.min_val <= value <= device.max_val, f"Ugyldig værdi: {value}"
        print("Alle værdier er gyldige")
        print("\n")

    def save_plot(self, filepath):
        plt.savefig(filepath)

##### Starter scriptet her #####
if __name__ == "__main__":
    DC = DataCollector()
    FS = FileSaving()

    ##### Definerer 3 typer af devices og hvilket værdi interval de må have #####
    ecg = Device(name="EKG Monitor", device_id="ecg", min_val=0, max_val=150)
    ppg = Device(name="Pulsmåler", device_id="ppg", min_val=40, max_val=200)
    temp = Device(name="Termometer", device_id="temp", min_val=35, max_val=41)

    ##### "Appender" devicesene så der kan genereres data for dem
    DC.add_device(ecg)
    DC.add_device(ppg)
    DC.add_device(temp)

    ##### Generer 200 målinger for hver enkelt device og udtrækker værdierne ######
    DC.collect_all(200)

    ecg_values = [m.value for m in ecg.measurements]
    ppg_values = [m.value for m in ppg.measurements]
    temp_values = [m.value for m in temp.measurements]
    
    ##### Plotter værdierne #####
    # Histogram
    plt.subplot(1, 3, 1)
    plt.hist(ecg_values, bins = 20)
    plt.title(ecg.name)
    plt.ylabel("Antal")
    plt.legend()
    
    plt.subplot(1, 3, 2)
    plt.hist(ppg_values, bins = 20)
    plt.title(ppg.name)
    plt.xlabel("Værdi")
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.hist(temp_values, bins = 20)
    plt.title(temp.name)
    plt.legend()

    FS.save_plot("Workshops/Workshop_1/Delopgave_2/files_generated/histogram.jpg")
    plt.show()


    # Boxplot
    plt.subplot(1,3,1)
    plt.boxplot(ecg_values)
    plt.title(ecg.name)
    plt.legend()

    plt.subplot(1,3,2)
    plt.boxplot(ppg_values)
    plt.title(ppg.name)
    plt.legend()

    plt.subplot(1,3,3)
    plt.boxplot(temp_values)
    plt.title(temp.name)
    plt.legend()

    FS.save_plot("Workshops/Workshop_1/Delopgave_2/files_generated/boxplot.jpg")
    plt.show()

    ##### Gem CSV filer #####
    for device in DC.devices:
        device_data = []
        for m in device.measurements:
            device_data.append([device.name, m.meas_id, m.timestamp, m.value]) 

        filename = f"Workshops/Workshop_1/Delopgave_2/files_generated/{device.name}_results.csv"
        FS.save_csv(filename, device_data)
    
    ##### Indlæser CSV/jpg filer og verificer at ingen data er gået tabt #####
    for device in DC.devices:
        filename = f"Workshops/Workshop_1/Delopgave_2/files_generated/{device.name}_results.csv"
        FS.load_csv(filename, device)

