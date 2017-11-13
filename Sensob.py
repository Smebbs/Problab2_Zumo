class Sensob:
    def __init__(self, sensors):
        self.sensors = sensors
        self.value = None

    def update(self):
        pass

    def reset(self):
        pass

    def get_value(self):
        return self.value
