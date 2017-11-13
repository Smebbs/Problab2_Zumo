class Kollisjon(Behavior):

    def __init__(self,bbcon,sensobs):
        super().__init__(bbcon,sensobs)

    def consider_activation(self):

        return True

    def consider_deactivation(self):

        return False

    def sense_and_act(self):
        sensor_value = self.sensobs.get_value()
        if sensor_value:
            motor_recommendation = None #Rygge + snu 180 grader + kjør framover
            match_degree = 0.9
            halt_request = False
        else:
            motor_recommendation = None
            match_degree = 0.01
            halt_request = False
        return motor_recommendation,match_degree,halt_request

