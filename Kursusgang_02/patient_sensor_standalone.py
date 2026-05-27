import random

class Patient:
    def __init__(self, hr):
        self.__hr = hr # Opgaven ka nogså løses med _hr, men så kan den ændres manuelt

    def update_from_sensor(self, hr_sensor):
        self.__hr = hr_sensor.measure()
    def get_hr(self):
        return self.__hr

class HeartRateSensor:
    def measure(self):
        hr_measure = random.randint(50,200)                                                                                                                                                   
        return hr_measure

hr_sensor = HeartRateSensor() # Denne henviser til værdien i update_from_sensor metoden

ole = Patient(0)
ole.update_from_sensor(hr_sensor)
ole.__hr = 100 # Kan ikke overskrive det, da det er privat

print(ole.get_hr()) # Skal bruge en get metode for at få privat værdi