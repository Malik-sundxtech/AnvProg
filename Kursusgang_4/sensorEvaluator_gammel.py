from fakeSensor import FakeSensor # Importer en klasse fra et script
from fakeSensor import Measurement
# https://stackoverflow.com/questions/28122963/typeerror-init-missing-2-required-positional-arguments-client-socket-a

class SensorEvaluator:
    def __init__(self, name, sensor = 0, sensor_id=0, sensor_type=0, device_id=0):
        self.name = name

    def tag_maalinger(self, mes):
        pass

    def kvalitets_test(self, mes=0, valid=0, invalid=0):
        for m in range (mes):
            if m.is_valid() #Funktion fra fakeSensor i Measurment
                valid = valid+1
            else:
                invalid = invalid+1
        validPer = valid/mes*100
            
        print(f"Measurements: {mes}")
        print(f"Valid: {valid}")
        print(f"Invalid: {invalid}")
        print(f"Valid Percentage: {validPer}%")
""" 
"""
        # if kval < 0.05
        # return Unacceptable
        # if kval > 0.05
        # return Acceptable
# SKAL HAVE FUNDET UD AF HVORDAN 



# Dette skal med:
evaluator = SensorEvaluator(
    sensor=FakeSensor(sensor_id="sensor-v1", sensor_type="PPG"),
    device_id="sensor-v1",
    name="Pulsmåler v1"
)

evaluator.tag_maalinger(mes=1000)   

measurement = Measurement.is_valid()

report = evaluator.kvalitets_test()








# print(evaluator)
# Mange målinger for pålidelig statistik! - skal lave 1000 målinger

# {
#   "total_measurements": 1000,
#   "valid": 980,
#   "invalid": 20,
#   "invalid_rate": 0.02, - skal være mindre end 0.05 for at være gyldig
#   "quality_score": "PASS" eller "FAIL", (Skal være mindre end 5% ugyldige målinger for at pass)
#   "mean": 75.3,
#   "min": 42,
#   "max": 198
# Test 1000 enheder 1000 gange
# 3 typer målinger PPG, blodtryk og temperatur
# }