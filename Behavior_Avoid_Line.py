from Reflectance import Reflectance



class Avoid_Line(Behavior):
    def __init__(self, bbcon, sensobs, color_grade=0.7):
        super().__init__(bbcon, sensobs)
        self.color_grade = color_grade


    def consider_activation(self):
        return True

    def consider_deactivation(self):
        return False
    
    def sense_and_act(self):
        values = self.sensob.get_value() # Få inn values fra sensob objektet
        dangers = filter(lambda x: x >= self.color_grade, values)

        motor_recommendation = None
        match_degree = None
        halt_request = False

        if len(dangers) > 0:
            motor_recommendation = 'Turn_Line'
            match_degree = 1
            halt_request = False

        return motor_recommendation, match_degree, halt_request
