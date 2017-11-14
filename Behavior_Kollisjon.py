from Behavior import Behavior


class Kollisjon(Behavior):

    def __init__(self,sensobs):
        super().__init__(sensobs)
        
     def consider_activation(self):
            if self.time == 0:
                if self.bbcon.future_collision:
                    self.time = 0
                    self.bbcon.activate_sensob(self.sensob)
                    return True
                else:
                    self.time = 1
            elif self.time == 1:
                self.time = 0
                self.bbcon.activate_sensob(self.sensob)
                return True


    def consider_deactivation(self):

        self.bbcon.deactivate_sensob(self.sensob)

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

