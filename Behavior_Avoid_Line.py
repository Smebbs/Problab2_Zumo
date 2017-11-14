from Reflectance import Reflectance
from Behavior import Behavior


class Avoid_Line(Behavior):
    def __init__(self, sensor, color_grade=0.7):
        super().__init__(sensor)
        self.sensor = sensor
        self.color_grade = color_grade


    def consider_activation(self):
         for sensob in self.sensobs:
                self.bbcon.activate_sensob(sensob)

    def consider_deactivation(self):
        return False
    
    def sense_and_act(self):
        values = self.sensor.get_value() # Få inn values fra sensob objektet
        filtered = []
        for value in values:
            if value >= self.color_grade:
                filtered.append(value)
        #dangers = filter(lambda x: x >= self.color_grade, values)

        motor_recommendation = 'N'
        match_degree = 0
        halt_request = False

        if len(filtered) > 0:
            motor_recommendation = 'B'
            match_degree = 1
            halt_request = False

        return motor_recommendation, match_degree, halt_request
