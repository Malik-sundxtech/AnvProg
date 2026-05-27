import matplotlib.pyplot as plt
import pandas as pd 

class PatientInfo:
    def __init__(self, name, gender, height_m, weight_kg, bmi): # Definerer parametrene i CSV filen
        self.name = name
        self.gender = str(gender)
        self.height_m = float(height_m) # Speciferer datatypen så de ikke laves om til strings
        self.weight_kg = float(weight_kg)
        self.bmi = float(bmi)
    def printInfo(self): # Laver en metode der kan printe informationerne
        print(f"{self.name:>20}, {self.gender:>6}, {self.height_m:>4.2f} m, {self.weight_kg:>2.0f} kg, BMI: {self.bmi:>.0f}") #Afgrænser hvor mange decimaler/bostaver der må vises


class MyLoader:
    def __init__(self, filename): # Definerer en filpath
        self.filename = filename
        
    def load_data(self) -> tuple[list,list]: # Skal retunere en liste af PatientInfo. Tuples gemmer flere variabler i en variabel
        data = [] # Der skal ikke bruges self. i tommelister, da der ellers ikke kan appendes i listen med self. 
        
        with open(self.filename, "r") as f: # Der anvendes en self.filename, da værdien skal gemmes her
            headers = f.readline().split(",") # Læser den første linje og seperer dem ved kommaerne
            for row in f:
                parts = row.split(",") # Tager hver linje seperer ordene ved komma
                p = PatientInfo(*parts) # Unpacker et datasæt med *
                data.append(p) # Datatype? Det finder den selv ud af åbenbart
            self.headers = headers
            self.data = data
            print(f"Data hentet fra {self.filename}")
        return(headers, data)
        
"""
"""
if __name__ == "__main__": # Dette gør at et andet program nemt kan køre denne funktion??
    #load = pd.read_csv("/home/Malik/Documents/Sundhedsteknologi/2. sem/Anvendt programmering/all_lectures/oop_3/files/exercise_people_small.csv")
    load = MyLoader("/home/Malik/Documents/Sundhedsteknologi/2. sem/Anvendt programmering/all_lectures/oop_3/files/exercise_people_small.csv")
    headers, data = load.load_data()

    for p in data:
        p.printInfo()


