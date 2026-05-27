class Device:
    def __init__(self, name, status):
        self.name = name
        self.__status = status

    def turn_on(self):
        self.__status = "ON"
    
    def turn_off(self):
        self.__status = "OFF"

    def get_status(self):
        return self.__status
        


EMG_monitor = Device("EMG Monitor", "OFF")
print(EMG_monitor.get_status())

EMG_monitor.__status = "ON" # Denne værdi kan ikke blive ændret gennem bruger input, da den er privat
print(EMG_monitor.get_status())

EMG_monitor.turn_on()
print(EMG_monitor.get_status())
