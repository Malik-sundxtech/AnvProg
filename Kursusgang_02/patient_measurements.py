class Patient:
    def __init__(self, id, heart_rate):
        self.id = id
        self.heart_rate = heart_rate

    def update_hr(self, updated_hr):
        self.heart_rate = updated_hr
    

karl = Patient(1, 150)
print(karl.heart_rate)



karl.update_hr(300)
print(karl.heart_rate)