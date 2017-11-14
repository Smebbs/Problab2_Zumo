from Behavior import Behavior


class Drive_Around(Behavior):

    def __init__(self):
        super().__init__("Sensor")
        self.bbcon = None

    def consider_activation(self):
        for sensob in self.sensobs:
               self.bbcon.activate_sensob(sensob)

    def consider_deactivation(self):

        return False

    def add_bbcon(self, bbcon):
        self.bbcon = bbcon

    def sense_and_act(self):
        self.bbcon.time +=1
        motor_recommendation = 'N'
        match_degree = 1
        if self.bbcon.time == 50:
            halt_request = True
        else:
            halt_request = False
        return motor_recommendation, match_degree, halt_request
