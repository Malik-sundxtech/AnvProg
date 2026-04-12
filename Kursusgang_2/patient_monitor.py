import random

class HeartRateSensor:
    def measure(self):
        val = random.randint(50,200)
        return val

class Patient:
    def __init__(self, id, heart_rate):
        self.id = id
        self.heart_rate = heart_rate

    def new_hr(self, sensor):
        self.heart_rate = sensor.measure()

class Monitor:
    def check(self, Patient):
        if Patient.heart_rate > 100:
           print("HIGH HR")

sensor = HeartRateSensor()

karl = Patient(1, 50)
karl.new_hr(sensor)

monitor = Monitor()    

monitor.check(karl)
print(karl.heart_rate)