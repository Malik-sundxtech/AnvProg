class Patient:
    def __init__(self, id:int, age:int, heart_rate:float): # De her type pins :float osv. er lidt ligemeget
        self.id = id
        self.age = age
        self._heart_rate = heart_rate

    def new_hr(self, new_hear_rate):
        if not isinstance(new_hear_rate, int): # Sikrer at der bruges den rigtige datatype
            raise ValueError(f"Datatypen var ikke et heltal {type(new_hear_rate)}")

        if not 0 < new_hear_rate < 250: # Sikrer at værdien er indenfor det korrekte arbejdsområde
            raise ValueError(f"Værdien skal være mellem 0 og 250 {new_hear_rate}")
           
        self._heart_rate = new_hear_rate


karl = Patient(1, 65, 72)

# karl.new_hr = float(input("New heart rate: "))  FIX THIS
karl._heart_rate = 69
print(karl._heart_rate)