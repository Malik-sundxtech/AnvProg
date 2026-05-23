""" Forkortelser
FS = FakeSensor
m = measurement
"""

# Importerer almene libraries
import numpy as np

# Importerer ønskede klasser
from fakeSensor import FakeSensor

# Definerer egen metode til at evaluere sensoren
class SensorEvaluator(): 
    def quality_report(validate_n, quality_score="FAIL"): # Uddbyende kvalitetscheck af 1 sensor
        for sensor_type in ["PPG", "BLOODPRESSURE", "TEMPERATURE"]: 

            # Loader de 3 sensorer PPG, BLOODPRESSURE og TEMPERATURE én ad gangen og foretager en måling på den
            print(f"=== {sensor_type} ===")
            FS = FakeSensor(sensor_type) 
            m = [FS.measure() for _ in range(validate_n)] 

            # Gemmer antallet valide og invalide målinger. Laver measurements om til tal, så der kan tages min og max af dem
            valid = [a for a in m if a.is_valid()] 
            invalid = [a for a in m if not a.is_valid()] 
            values = [a.value for a in m] 
            
            # Kvalitetescheck, den skal have mere end 95% korrekte målinger for at bestå
            if len(valid)/len(m) > 0.95: 
                quality_score = "PASS"
            else:
                quality_score = "FAIL"
            
            # Printer forskellige mål for sensoren
            print(f"Valid: {len(valid)}")
            print(f"Invalid: {len(invalid)}")
            
            print(f"Validity rate: {len(valid) / len(m)*100:.2f} %")
            print(f"Invalidity rate: {len(invalid) / len(m)*100:.2f} %")
            print(f"Quality score: {quality_score}")

            print(f"Minimum value: {np.min(values)}")
            print(f"Maximum value: {np.max(values)}")
            print("\n")


    def evaluate(sensor_n, validate_n, passed_sensors=0): # Tjekker mange sensorer
        for sensor_type in ["PPG", "BLOODPRESSURE", "TEMPERATURE"]:
            print(f"=== {sensor_type} sensors ===")
            passed_sensors = 0

            # Tester hver sensor n gange og giver en score af hvor mange sensorer der bestod
            for i in range(sensor_n):

                FS = FakeSensor(sensor_type) 
                m = [FS.measure() for _ in range(validate_n)]
                valid = [a for a in m if a.is_valid()]
                
                if len(valid)/len(m) >= 0.95:
                    passed_sensors += 1

            # Printer procentsatsen af sensorer der bestod
            print(f"Numbers of {sensor_type} sensors passed the test: {passed_sensors / sensor_n*100} % ")
            print("\n")


# Kører scriptet herinde
if __name__ == "__main__":
    SensorEvaluator.quality_report(1000) # sensorer testes 1000 gange
    SensorEvaluator.evaluate(1000, 1000) # 1000 sensorer testes 1000 gange

    
""" Besvarelse af spørgsmål
Hvorfor er 1000 målinger bedre end 10 målinger?
    Større datagrundlag, 1 fejlmåling vil give et meget større udsving ud af 10 end det vil ved 1000

Hvis 5 sensorer har mellem 1.8%-2.3% fejl, kan du stole på at de næste 100 sensorer også vil have det?
    De næse 100 sensorer vil nok ligge i den bold gade hvis hver sensor er testet 1000 gange, men man er aldrig garanteret dette

Hvad hvis hospitalet kræver <1% fejl? Skal I redesigne sensoren?
    Den enkelte sensor har en validitet på mellem 95-100% ved gennemgang. Så det kræver nok et nyt design
"""