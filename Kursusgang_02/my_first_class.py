class Device:
    def __init__(self, name, status):
        self.name = name
        self.status = status

pc = Device("Maliks pc", "OFF")

print(pc.name, pc.status)
