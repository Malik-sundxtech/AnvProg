import matplotlib.pyplot as plt
import my_loader as ml # Importetrer og anvender et pythonscript på sammevis som andre pakker

class MyDataVisualizer:
    def __init__(self, headers:list, data:list): 
        self.headers = headers
        self.data: list[ml.PatientInfo] = data # Obs på syntax her, ellers kan den ikke læse variablenre e.g. height_m herfra
        
    def scatterplot(self):
        heights_male = [p.height_m for p in self.data if p.gender == "male"]
        weight_male = [p.weight_kg for p in self.data if p.gender == "male"]
        heights_female = [p.height_m for p in self.data if p.gender != "male"]
        weight_female = [p.weight_kg for p in self.data if p.gender != "male"]
        
        plt.scatter(heights_male, weight_male, label ="Male")
        plt.scatter(heights_female, weight_female, label="Female")
        plt.legend()
        plt.xlabel("Height (m)")
        plt.ylabel("Weight (kg)")
        plt.title("Titel :)")
        plt.show()
    


dataloader = ml.MyLoader("/home/Malik/Documents/Sundhedsteknologi/2. sem/Anvendt programmering/all_lectures/oop_3/files/exercise_people_small.csv")
header, data = dataloader.load_data()
data_visualizer = MyDataVisualizer(header, data) # Det er vigtigt at header og data kaldes i samme rækkefølge som de er defineret i __init__

data_visualizer.scatterplot()