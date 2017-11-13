import sensob

class Ultra(Sensob):
    def __init__(self, sensors):
        super().__init__(sensors)

    def get_value(self):
        values = []
        for sensor in self.sensors:  # Update og append values
            sensor.update()
            values.append(sensor.getvalue)
        limit = 0.01  # placeholder verdi
        danger_flag = False
        for value in values:
            if value < limit:
                danger_flag = True
        return danger_flag

