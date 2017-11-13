from Behavior import Behavior


class Kollisjon(Behavior):

    def __init__(self,sensobs):
        super().__init__(sensobs)

    def consider_activation(self):

        return True

    def consider_deactivation(self):

        return False

    def sense_and_act(self):
        sensor_value = self.sensobs.get_value()
        if sensor_value:
            motor_recommendation = "B" #Rygge + snu 180 grader + kjør framover
            match_degree = 1
            halt_request = False
        else:
            motor_recommendation = "N"
            match_degree = 0.01
            halt_request = False
        return motor_recommendation,match_degree,halt_request

