import random 
from datetime import datetime 
import matplotlib.pyplot as plt
import csv

class Measurement:
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value

class Device(): # Template til devices
    def __init__(self, device_id, name, min_val, max_val):
        self.device_id = device_id
        self.name = name
        self.min_val = min_val
        self.max_val = max_val
        self.measurements = []

    def generate_measurement(self):
        value = random.uniform(self.min_val, self.max_val)

        measurement = Measurement(timestamp=datetime.now(), value=value)

        self.measurements.append(measurement)





class DataCollector(): # Saml data i en CSV fil
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def collect_all(self, n_measurements):
        for device in self.devices:
            for _ in range(n_measurements):
                device.generate_measurement()







if __name__ == "__main__":
    DC = DataCollector()


    ecg = Device(device_id="ecg_001", name="EKG Monitor", min_val=0, max_val=150)
    ppg = Device(device_id="ppg_001", name="Pulsmåler", min_val=40, max_val=200)
    temp = Device(device_id="temp_001", name="Termometer", min_val=35, max_val=41)

    DC.add_device(ecg)
    DC.add_device(ppg)
    DC.add_device(temp)

    DC.collect_all(10)
    plt.plot()