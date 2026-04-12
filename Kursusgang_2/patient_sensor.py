import random

class HeartRateSensor:
    def measure(self):
        val = random.randint(50,200)
        return val
    
    
class Patient:
    def __init__(self, id:int, age:int, heart_rate:float): # De her type pins :float osv. er lidt ligemeget
        self.id = id
        self.age = age
        self.heart_rate = heart_rate

    def new_hr(self, sensor):
        self.heart_rate = sensor.measure()


sensor = HeartRateSensor()

karl = Patient(1, 65, 72)

karl.new_hr(sensor)

print(karl.heart_rate)