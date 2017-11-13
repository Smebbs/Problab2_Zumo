class Sensob:
    def __init__(self, sensors):
        self.sensors = sensors
        self.value = None

    def update(self, value):
        self.value = value

    def get_value(self):
        return self.value
