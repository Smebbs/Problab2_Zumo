from Sensob import Sensob
from ultrasonic import Ultrasonic

class Ultra(Sensob):
    def __init__(self, sensors):
        super().__init__(sensors)
        self.sensors = sensors

    def get_value(self):
        values = []
 # Update og append values
        value = self.sensors.update()
        #values.append(self.sensors.get_value())
        danger_limit = 0.01  # placeholder verdi
        future_limit = 0.50 #placeholder verdi
        danger_flag = False
        future_collision = False
        print("Value: ", value)
        if value < danger_limit:
           danger_flag = True
        if value < future_limit:
            future_collision = True
        return danger_flag,future_collision


