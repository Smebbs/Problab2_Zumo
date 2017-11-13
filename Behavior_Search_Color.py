class Search_Color(Behavior):
    def __init__(self, bbcon, sensobs):
        super().__init__(bbcon, sensobs)
        self.time = 0

    def consider_activation(self):
        if self.time == 0:
            self.time += 1
            return False
        elif self.time == 1:
            self.time = 0
            return True

    def consider_deactivation(self):
        return True

    def sense_and_act(self):
        image = self.sensobs.get_value()
        #Bruk metode på bildet for å finne hvor fargen er i bildet og bruk dette som angle
        motor_recommendation = 'Turn_Color'
        match_degree = None #Juster utfra angle
        halt_request = False
        return motor_recommendation, match_degree, halt_request
