class Device:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

EMG_monitor = Device("EMG monitor", "OFF")

EMG_monitor.turn_on()

print(EMG_monitor.name, EMG_monitor.status)