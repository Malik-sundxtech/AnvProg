class PersonInfo:
    def __init__(self, name, dob, sys_bp, dia_bp, ef_percent):
        self.name = name
        self.dob = dob
        self.sys_bp = sys_bp
        self.dia_bp = dia_bp
        self.ef_percent = ef_percent
    def showInfo(self):
        print(f"Navn: {self.name}")
        print(f"Date of birth: {self.dob}")
        print(f"Systole: {self.sys_bp}")
        print(f"Diastole: {self.dia_bp}")
        print(f"Ef percent: {self.ef_percent}")

#person = PersonInfo("Karl","05/12/1998", 120, 80, "50%")

person = PersonInfo(
    name="Karl", 
    dob="05/12/1998", 
    sys_bp=120, 
    dia_bp=80, 
    ef_percent="55%"
)
person.showInfo()    
