import random

class HeartRateSensor():
    def measure(self):
        return random.randint(50, 200)
    
class Patient():
    def __init__(self, id, hr=0):
        self.id = id
        self.hr = hr
    def update_hr(self, hr_sensor):
        self.hr = hr_sensor.measure()

class Monitor():
    def check(self, patient): #patient her er blot en variabel og ikke klasse
        if patient.hr > 150:
            print(f"Patient {patient.id} har høj puls")

patients = [Patient(1), Patient(2), Patient(3)]
hrsensor = HeartRateSensor()
monitor = Monitor()

for p in patients:
    p.update_hr(hrsensor)

for p in patients:
    print(f"Patient {p.id} has a hr: {p.hr}")
    monitor.check(p)

# for patient, sensor in zip(patients, sensors):
#     patient.update_from_sensor(sensor)
#     monitor.check(patient)
# zip er en funktion der gør det muligt at tage flere lister
# patient og sensor kunne lige så godt være i og j, det er bare andre navne