class Patient:
    def __init__(self, id:int, age:int, heart_rate:float): # De her type pins :float osv. er lidt ligemeget
        self.id = id
        self.age = age
        self.heart_rate = heart_rate

    def new_hr(self, new_hear_rate):
        self.heart_rate = new_hear_rate

    def __str__(self):
        return f"Patient(id={self.id}, age={self.age}, heartrate={self.heart_rate})"
karl = Patient(1, 65, 72)

print(karl.id)
print(karl.age)

karl.new_hr = float(input("New heart rate: ")) # Denne virker ikke lige, fejl søg
# karl.new_hr(input("New heart rate: "))

print(karl.heart_rate)

# karl.__str__ FÅ DET HER TIL AT VIRKE, hvor jeg printer dem alle med en dunder string.
