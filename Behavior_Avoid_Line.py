class Avoid_Line(Behavior):
    def __init__(self, bbcon, sensobs):
        super().__init__(bbcon, sensobs)

    def consider_activation(self):
        return True

    def consider_deactivation(self):
        return False
    
    def sense_and_act(self):
        values = None # Få inn values fra sensob objektet 
        #Sett angle utfra values
        motor_recommendation = 'Turn_Line'
        match_degree = None #Juster utfra angle
        halt_request = False
        return motor_recommendation, match_degree, halt_request
