import sensob

class Ultra(Sensob):
    def __init__(self, sensors):
        super().__init__(sensors)

    def get_value(self):
        values = []
        for sensor in self.sensors:  # Update og append values
            sensor.update()
            values.append(sensor.getvalue)
        danger_limit = 0.01  # placeholder verdi
        future_limit = 0.50 #placeholder verdi
        danger_flag = False
        future_collision = False
        for value in values:
            if value < danger_limit:
                danger_flag = True
            if value < future_limit:
                future_collision = True
        return danger_flag,future_collision
