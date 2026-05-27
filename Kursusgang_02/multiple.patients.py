import random

class Patient():
    def __init__(self, id, hr = 0): # Her sætter jeg en værdi for alles hr
        self.id = id
        self.hr = hr
    def update_from_hrsensor(self, hr_sensor):
        self.hr = hr_sensor.measure_hr()

class HeartRateSensor():
    def measure_hr(self):
        return random.randint(50,200)
    
hr_sensor = HeartRateSensor()

patients = [Patient(1), Patient(2), Patient(3)] #
    

for p in patients:
    p.update_from_hrsensor(hr_sensor) # Loop der opdatere alles hr

for p in patients:
    print(f"Patient {p.id} has a hr: {p.hr}") # Den antager automatisk at p er for patients[p]