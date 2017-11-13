class Drive_Around(Behavior):
    
    def __init__(self, bbcon, sensobs):
        super().__init__(bbcon, sensobs)
    
    def consider_activation(self):

        return True

    def consider_deactivation(self):

        return False

    def sense_and_act(self):
        motor_recommendation = 'Standard'
        match_degree = 1
        halt_request = False
        return motor_recommendation, match_degree, halt_request
        
