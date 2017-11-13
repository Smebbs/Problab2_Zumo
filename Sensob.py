class Sensob:
    def __init__(self, sensors):
        self.sensors = sensors
        self.value = None

    def update(self):
        return self.get_value()

    def get_value(self):
        return
