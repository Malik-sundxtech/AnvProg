import math
import numpy as np
import scipy as sp
import sklearn as sk

from fakeSensor import FakeSensor, Measurement




class SensorEvaluator():
    pass

#fs = FakeSensor() # Skal ikke lave det til et objekt?
#ms = Measurement()

if __name__ == "__main__":
    sensor = FakeSensor(sensor_id="dev-001", sensor_type="PPG")
    print(f"\n=== {sensor.sensor_type} Sensor ===")
    
    
